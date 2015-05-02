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
      
class Encrypto(object):
  global ALL_KEYS     
  global ALPHA_MATRIX  

  def __init__(self):

    self.SMALL_ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m'\
                       ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

    self.CAP_ALPHA   = ['A','B','C','D','E','F','G','H','I','J','K','L','M'\
                       ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    self.NUMBERS     = ['1','2','3','4','5','6','7','8','9','0']

    self.OTH_KEYS    = [' ','`','~','!','@','#','$','%','^','&','*','(',')',\
                       '-', '_','=','+','[','{',']','}','\\','|',';',':',\
                       '\'','\"',',','<','.','>','/','?',']',]

    self.ALL_KEYS = self.SMALL_ALPHA + self.CAP_ALPHA + self.NUMBERS + self.OTH_KEYS  

    self.ALPHA_MATRIX = [self.alphaShift(MOD) for MOD in range(len(self.ALL_KEYS))]


    self.header()
    while True:
      self.main()        
            



  def header(self):
  	print("")
  	print ("+===============================================================+")
  	print ("|                                                               |")
  	print ("|                                                               |")
  	print ("|               --- Welcome to Encrypto v0.6 ---                |")
  	print ("|                                                               |")
  	print ("|                                                        //AXAY |")
  	print ("+===============================================================+")
  	print("")




  def getText(self):
          try:
            print("Enter text")
            inp = str(input("> "))
          except:
            TypeError or ValueError ("Enter a valid text. Try again.")
            self.getText()

          while len(inp)==0:
                  print("You must enter something to proceed! Try again.")
                  inp=str(input("> "))
          print("")
          return inp

               

  def getKey(self, text):       
          

          try:
            print("Enter key")
            key=str(input("> "))
          except:
            TypeError or ValueError ("Enter a valid key. Try again.")
            self.getKey(text)

          while len(key)== 0:
                  print("You must enter a key! Try again.")
                  key=str(input("> "))
          print("")

          if len(key)<len(text):
                  temp=key                
                  i=0
                  while len(temp)<len(text):
                          temp=temp+key[(i%len(key))]
                          i=i+1
                  key=temp
                          
          elif len(key)>len(text):
                  temp=""
                  for i in range(len(text)):
                          temp=temp+key[(i%len(key))]
                  key=temp
          
          return key

                  
  def alphaShift(self,x): 
    global ALL_KEYS

    if x<=len(self.ALL_KEYS) and x>-1:
    	res=[]
    	for item in range(len(self.ALL_KEYS)-x):
    		res.append(self.ALL_KEYS[item+x])
    	
    	for item in range(x):
    		res.append(self.ALL_KEYS[item-len(self.ALL_KEYS)])

    	return res

    else:
    	raise ValueError("Parameter for alphaShift must be >-1 and <"+str(len(ALL_KEYS)+1))



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



  def main(self):	 
          print("Menu: ")
          print("--------------------")
          print("[1] Encrypt a text")
          print("[2] Decrypt a cipher")
          print("[3] Exit")
          print("")

          inp=str(input("Your response > "))

          print ("")

          if inp=="1":
                  text = self.getText()
                  key = self.getKey(text)
                  print("Encrypted cipher: "+ self.encrypt(text, key))
                  print("")

          elif inp=="2":
                  text = self.getText()
                  key = self.getKey(text)
                  print("Decrypted text: " + self.decrypt(text, key))
                  print("")

          elif inp=="3":
                  print("Bye!")
                  print("")
                  raise SystemExit
                  
          else:
                  print("Invalid response. Try again. Enter option # only.")
                  print("")
                  self.main()

if __name__ == '__main__':
  Encrypto()
