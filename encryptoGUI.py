#!/usr/bin/python
# ‐*‐ coding: utf‐8 ‐*‐
#Supports Python3.x only

__author__="Akshay"

"""

</AXAY>
<www.akshayjha.co.nr>
<www.GitHub.com/AxayJha>
<akshayjha@live.in>
Last modified: 01/05/2015

//The Encrypto Project
Version 0.7

Under GNU LGPL v3.0 License.
Free to use, modify and distribute! 

"""


from tkinter import *

global ALL_KEYS     
global ALPHA_MATRIX  

  

SMALL_ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m'\
              ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

CAP_ALPHA   = ['A','B','C','D','E','F','G','H','I','J','K','L','M'\
              ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

NUMBERS     = ['1','2','3','4','5','6','7','8','9','0']

OTH_KEYS    = [' ','`','~','!','@','#','$','%','^','&','*','(',')',\
               '-', '_','=','+','[','{',']','}','\\','|',';',':',\
               '\'','\"',',','<','.','>','/','?',']','\n']

ALL_KEYS = SMALL_ALPHA + CAP_ALPHA + NUMBERS + OTH_KEYS  

                
def alphaShift(x): 

  global ALL_KEYS

  if x <= len(ALL_KEYS) and x > -1:

  	res=[]

  	for item in range (len( ALL_KEYS ) - x):
  		res.append ( ALL_KEYS[ item + x ] )
  	
  	for item in range (x):
  		res.append ( ALL_KEYS[ item - len(ALL_KEYS)] )

  	return res

  else:
  	raise ValueError ("Parameter for alphaShift must be > -1 and < "+str(len(ALL_KEYS)+1))

##---------------------------------------------------------------------------------------

ALPHA_MATRIX = [ alphaShift(MOD) for MOD in range(len(ALL_KEYS)) ]

##---------------------------------------------------------------------------------------
	

def keylen(key, text):

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


def encrypt(text, key): 

	CIPHER=""

	dimensionOne=[]
	dimensionTwo=[]

	for i in range(len( text )):
		for j in range(len( ALPHA_MATRIX[0] )):

			if ALPHA_MATRIX[0][j] == text[i]:
				dimensionOne.append(j)



	for k in range(len( key )):
		for l in range(len( ALPHA_MATRIX[0] )):

			if ALPHA_MATRIX[0][l] == key[k]:
				dimensionTwo.append(l)


	for n in range(len( dimensionOne )):
		CIPHER += ALPHA_MATRIX [dimensionOne[n]] [dimensionTwo[n]]			


	return CIPHER



def decrypt(cipher, key):  
	DEC_CIPHER=""

	dimensionOne=[]
	dimensionTwo=[]

	for j in range(len( key )):
		for i in range(len( ALPHA_MATRIX )):

			if ALPHA_MATRIX[i][0] == key[j]:
				dimensionOne.append(i)

	for j in range(len( cipher )):
		for i in range(len( ALPHA_MATRIX[0] )):

			if cipher[j] == ALPHA_MATRIX [ dimensionOne[j] ] [i]:
				dimensionTwo.append(i)

			

	for n in range(len( dimensionTwo )):
		DEC_CIPHER += ALPHA_MATRIX[0] [ dimensionTwo[n] ]

	return DEC_CIPHER

	
##----------------------------------------GUI Design-----------------------------------------------


root = Tk()

try:
	root.iconbitmap (default='icon.ico')
except:
	pass
	
root.geometry   ('480x500+300+200')
root.title      ("Encrypto v0.7")


headFrame   = Frame(root, bg="darkblue", width=150, height=45)
topFrame    = Frame(root, bg="darkred" , width=150, height=130)
midFrame    = Frame(root, bg="grey"    , width=150, height=130)
bottomFrame = Frame(root, bg="darkgrey", width=150, height=145)

headFrame.pack   (fill=X)
topFrame.pack    (fill=X, padx=5, pady=5)
midFrame.pack    (fill=X, padx=5, pady=5)
bottomFrame.pack (fill=X, padx=5, pady=5)


head        = Label(headFrame, text="Encrypto")
head.pack(side=LEFT)

try:
	photo       = PhotoImage (file="key.gif")
	label       = Label      (headFrame, image=photo, height=40 )
	label.image = photo
	label.pack()

except :
	pass


textLabel   = Label(topFrame   , text="Text: "   , width=20)
keyLabel    = Label(midFrame   , text="Key: "    , width=20)
ResultLabel = Label(bottomFrame, text="Result: " , width=20)

"""entry1=StringVar()
textEntry1= Entry(topFrame, textvariable=entry1)

entry2=StringVar()
textEntry2= Entry(midFrame, textvariable=entry2)"""

resultBox = Text (bottomFrame, height=7, width=48)
getText1  = Text (topFrame   , height=7, width=48)
getText2  = Text (midFrame   , height=7, width=48)

textLabel.grid   (row=0, column=0)
keyLabel.grid    (row=1, column=0)
ResultLabel.grid (row=2, column=0)
getText1.grid    (row=0, column=1)
getText2.grid    (row=1, column=1)
resultBox.grid   (row=2, column=1)


def exit():
	raise SystemExit


menu = Menu(root)
root.config (menu = menu)

fileMenu = Menu(menu)
menu.add_cascade     (label="File", menu=fileMenu)
fileMenu.add_command (label="Exit", command=exit )


global i
i=1

def select1():
	global i	
	i=1
	option2.deselect()
	buttontext.set("Encrypt")
	

def select2():
	global i	
	i=2
	option1.deselect()
	buttontext.set("Decrypt")
	


var = IntVar()
option1 = Checkbutton(bottomFrame, text="Encrypt", command=select1)
option1.grid (row=3, sticky=E)

var1 = IntVar()
option2 = Checkbutton(bottomFrame, text="Decrypt", command=select2)
option2.grid (row=4, sticky=E)



def clicked():
	input = getText1.get ("1.0", END)
	text  = str(input)

	if text.endswith("\n") == True:
		text = text[:-1]
	##text = text.replace("\n","")

	input   = getText2.get("1.0", END)
	tempkey = str(input)

	tempkey = tempkey.replace ("\n"   , ""  )
	key     = keylen          (tempkey, text)
	

	if i==1:
		resultBox.delete ("1.0", END)
		result = encrypt (text , key)

		if len(result) > len(text):
			result = result[:(len(text))]

		resultBox.insert(INSERT, result)
		buttontext.set  ("Encrypt")

	elif i==2:
		resultBox.delete  ("1.0", END)
		result =  decrypt (text , key)

		if len(result) > len(text):
			result = result[:(len(text))]

		resultBox.insert (INSERT, result)
		buttontext.set   ("Decrypt")


buttontext = StringVar()

if   i==1:
	buttontext.set ("Encrypt")

elif i==2:		
	buttontext.set ("Decrypt")


button = Button (bottomFrame, textvariable=buttontext, command=clicked)
button.grid     (row=4, column=1, sticky=E)



root.mainloop()
