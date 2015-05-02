#!/usr/bin/python
# ‐*‐ coding: utf‐8 ‐*‐
#Supports Python3.x only

__author__="Akshay"

"""

</AXAY>
<www.akshayjha.co.nr>
<www.GitHub.com/AxayJha>
<akshayjha@live.in>
Last modified: 02/05/2015

//The Encrypto Project
v0.7.3

Under GNU LGPL v3.0 License.
Free to use, modify and distribute! 
"""

from tkinter import *


class Encrypto(object):  

	def __init__(self):

		##-----------------------------------97 X 97 Matrix----------------------------------------

		global ALL_KEYS     
		global ALPHA_MATRIX  


		self.SMALL_ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m'\
		                   ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

		self.CAP_ALPHA   = ['A','B','C','D','E','F','G','H','I','J','K','L','M'\
		                   ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

		self.NUMBERS     = ['1','2','3','4','5','6','7','8','9','0']

		self.OTH_KEYS    = [' ','`','~','!','@','#','$','%','^','&','*','(',')',\
		                   '-', '_','=','+','[','{',']','}','\\','|',';',':',\
		                   '\'','\"',',','<','.','>','/','?',']','\n']

		self.ALL_KEYS = self.SMALL_ALPHA + self.CAP_ALPHA + self.NUMBERS + self.OTH_KEYS  

		self.ALPHA_MATRIX = [ self.alphaShift(MOD) for MOD in range(len(self.ALL_KEYS)) ]

		##-------------------------------------GUI design-------------------------------------------

		self.root = Tk()

		try:
			self.root.iconbitmap (default='icon.ico')
		except:
			pass

			
		self.root.geometry   ('570x500+300+200')
		self.root.title      ("Encrypto v0.7")


		self.headFrame   = Frame(self.root, bg="darkblue", width=150, height=45)
		self.topFrame    = Frame(self.root, bg="darkred" , width=150, height=130)
		self.midFrame    = Frame(self.root, bg="grey"    , width=150, height=130)
		self.bottomFrame = Frame(self.root, bg="darkgrey", width=150, height=145)

		self.headFrame.pack   (fill=X)
		self.topFrame.pack    (fill=X, padx=5, pady=5)
		self.midFrame.pack    (fill=X, padx=5, pady=5)
		self.bottomFrame.pack (fill=X, padx=5, pady=5)


		self.head        = Label(self.headFrame, text="Encrypto")
		self.head.pack(side=LEFT)


		try:
			self.photo       = PhotoImage (file="key.gif")
			self.label       = Label      (self.headFrame, image=self.photo, height=40 )
			self.label.image = self.photo
			self.label.pack()

		except :
			pass


		self.textLabel   = Label(self.topFrame   , text="Text: "   , width=20)
		self.keyLabel    = Label(self.midFrame   , text="Key: "    , width=20)
		self.ResultLabel = Label(self.bottomFrame, text="Result: " , width=20)

		self.resultBox = Text (self.bottomFrame, height=7, width=48)
		self.getText1  = Text (self.topFrame   , height=7, width=48)
		self.getText2  = Text (self.midFrame   , height=7, width=48)

		self.textLabel.grid   (row=0, column=0)
		self.keyLabel.grid    (row=1, column=0)
		self.ResultLabel.grid (row=2, column=0)
		self.getText1.grid    (row=0, column=1)
		self.getText2.grid    (row=1, column=1)
		self.resultBox.grid   (row=2, column=1)

		self.menu = Menu(self.root)
		self.root.config (menu = self.menu)

		self.fileMenu = Menu(self.menu)
		self.menu.add_cascade     (label="File", menu=self.fileMenu)
		self.fileMenu.add_command (label="Exit", command=self.exit )


		global i
		self.i=1


		self.var = IntVar()
		self.option1 = Checkbutton(self.bottomFrame, text="Encrypt", command=self.select1)
		self.option1.grid (row=3, sticky=E)

		self.var1 = IntVar()
		self.option2 = Checkbutton(self.bottomFrame, text="Decrypt", command=self.select2)
		self.option2.grid (row=4, sticky=E)

		self.buttontext = StringVar()


		if   self.i==1:
			self.buttontext.set ("Encrypt")

		elif self.i==2:		
			self.buttontext.set ("Decrypt")


		self.button = Button (self.bottomFrame, textvariable=self.buttontext, command=self.clicked)
		self.button.grid     (row=4, column=1, sticky=E)


		self.root.mainloop()

	#-------------------------------------------The Methods-----------------------------------------------
	                
	def alphaShift(self, x): 

	  global ALL_KEYS

	  if x <= len(self.ALL_KEYS) and x > -1:

	  	res=[]

	  	for item in range (len( self.ALL_KEYS ) - x):
	  		res.append ( self.ALL_KEYS[ item + x ] )
	  	
	  	for item in range (x):
	  		res.append ( self.ALL_KEYS[ item - len(self.ALL_KEYS)] )

	  	return res

	  else:
	  	raise ValueError ("Parameter for alphaShift must be > -1 and < "+str(len(ALL_KEYS)+1))

		

	def keylen(self, key, text):

		if len(key) < len(text):
		    temp = key                
		    i    = 0

		    while len(temp)<len(text):
		        temp += key[ (i % len(key)) ]
		        i += 1

		    key = temp
		                        
		elif len(key) > len(text):
		    temp = ""

		    for i in range(len(text)):
		        temp += key[(i%len(key))]

		    key = temp

		return key



	def encrypt(self, text, key): 

		CIPHER=""

		dimensionOne=[]
		dimensionTwo=[]

		for i in range(len( text )):
			for j in range(len( self.ALPHA_MATRIX[0] )):

				if self.ALPHA_MATRIX[0][j] == text[i]:
					dimensionOne.append(j)



		for k in range(len( key )):
			for l in range(len( self.ALPHA_MATRIX[0] )):

				if self.ALPHA_MATRIX[0][l] == key[k]:
					dimensionTwo.append(l)


		for n in range(len( dimensionOne )):
			CIPHER += self.ALPHA_MATRIX [dimensionOne[n]] [dimensionTwo[n]]			


		return CIPHER



	def decrypt(self, cipher, key):  
		DEC_CIPHER=""

		dimensionOne=[]
		dimensionTwo=[]

		for j in range(len( key )):
			for i in range(len( self.ALPHA_MATRIX )):

				if self.ALPHA_MATRIX[i][0] == key[j]:
					dimensionOne.append(i)

		for j in range(len( cipher )):
			for i in range(len( self.ALPHA_MATRIX[0] )):

				if cipher[j] == self.ALPHA_MATRIX [ dimensionOne[j] ] [i]:
					dimensionTwo.append(i)

				

		for n in range(len( dimensionTwo )):
			DEC_CIPHER += self.ALPHA_MATRIX[0] [ dimensionTwo[n] ]

		return DEC_CIPHER

		

	def exit(self):
		raise SystemExit

	
	def select1(self):
		global i	
		self.i=1
		self.option2.deselect()
		self.buttontext.set("Encrypt")
		

	def select2(self):
		global i	
		self.i=2
		self.option1.deselect()
		self.buttontext.set("Decrypt")
		

	def clicked(self):
		input = self.getText1.get ("1.0", END)
		text  = str(input)

		if text.endswith("\n") == True:
			text = text[:-1]
		
		input   = self.getText2.get("1.0", END)
		tempkey = str(input)

		tempkey = tempkey.replace ("\n"   , ""  )
		key     = self.keylen          (tempkey, text)
		

		if self.i==1:
			self.resultBox.delete ("1.0", END)
			result = self.encrypt (text , key)

			if len(result) > len(text):
				result = result[:(len(text))]

			self.resultBox.insert(INSERT, result)
			self.buttontext.set  ("Encrypt")

		elif self.i==2:
			self.resultBox.delete  ("1.0", END)
			result =  self.decrypt (text , key)

			if len(result) > len(text):
				result = result[:(len(text))]

			self.resultBox.insert (INSERT, result)
			self.buttontext.set   ("Decrypt")

#-----------------------------------------------Here we GO!--------------------------------------------------
	
if __name__ == '__main__':
	Encrypto()
