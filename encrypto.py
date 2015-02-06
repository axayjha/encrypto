## <AXAY/>
## <akshayjha@live.in>
## <fb.com/AxayJha>

##------------------------GNU LESSER GENERAL PUBLIC LICENSE-------------------
def gplp1():
	"""            GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License. """
	
def gplp2():
  """ "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version."""

def gplp3():
  """ The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL."""
  
def gplp4():  
  """ 2. Conveying Modified Versions.
  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy."""
  
def gplp5():
  """ 3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document."""
  
def gplp6():
  """4. Combined Works.
  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:
   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.
   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.
   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document."""
  
def gplp7():
   """d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version."""
   
def gplp8():
   """e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)"""
   
def gplp9():
  """5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work."""
  
def gplp10():
  """6. Revised Versions of the GNU Lesser General Public License.
  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.
  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation."""

def gplp11():

 """ If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library."""
 
##---------------------------------------------------------------------------

def main(page):
    if page==0:
        print(gplp1.__doc__)  
    elif page==1:
        print(gplp2.__doc__) 
    elif page==2:
        print(gplp3.__doc__)
    elif page==3:
        print(gplp4.__doc__)
    elif page==4:
        print(gplp5.__doc__)
    elif page==5:
        print(gplp6.__doc__)
    elif page==6:
        print(gplp7.__doc__)
    elif page==7:
        print(gplp8.__doc__)
    elif page==8:
        print(gplp9.__doc__)
    elif page==9:
        print(gplp10.__doc__)
    elif page==10:
        print(gplp11.__doc__)     
  
def gnugpl():
    global pag
    pag=0
    def resp():
        global pag
        if pag<1:
                print("1. Next, 3. Exit")
        elif pag>9:
                print("2. Back, 3. Exit")
        else:            
                print("1. Next, 2. Back, 3. Exit" )
        inp = str(input("Your response: "))
        print("")
        if inp == "1":
            pag=pag+1
        elif inp=="2":
            pag=pag-1 
        elif inp == "3":
            while True:
                    menu()

        else:
            print("Invalid Response")
            print("")
            resp() 
          
    while pag<=11:
        if pag<0:
            pag=0
        if pag>10:
                pag=10
        print("")
        print("-------------------------------------Page " + str(pag+1) + "------------------------------------")
        print("")
        main(pag)
        print("")
        print("Page: " + str(pag+1))
        print("--------------------------------------------------------------------------------")
        resp()
        
##---------------------------------------------------------------------------------

        ##               PROGRAM STARTS HERE
        ##              ---------------------
        
##_________________________________________________________________________________
        
global text    ## works as input text while encrypting and vignere cipher while decrypting
global key     ## the key used to enncrypt or decrypt a text
global al      ## defined in line 263
global alphmat ##the 96 * 96 matrix of all possible inputs (al)
##----------------------------------------------------------------------------------

sAl=['a','b','c','d','e','f','g','h','i','j','k','l','m'\
,'n','o','p','q','r','s','t','u','v','w','x','y','z']
cAl=['A','B','C','D','E','F','G','H','I','J','K','L','M'\
,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['1','2','3','4','5','6','7','8','9','0']
others=[' ','`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[','{',']','}','\\','|',';',':','\'','\"',',','<','.','>','/','?',']',]

al=sAl+cAl+num+others ##list of all inputs possible from a 96 key keyboard
##-----------------------------------------------------------------------------------

def header():
	print("")
	print ("+===============================================================+")
	print ("|                                                               |")
	print ("|                                                               |")
	print ("|               --- Welcome to Encrypto v0.5 ---                |")
	print ("|                                                               |")
	print ("|                                                        //AXAY |")
	print ("+===============================================================+")
	print("")
##------------------------------------------------------------------------------------
	
def getinp():       ##implement to get the input text or cipher and the key
        global text
        global key
        text=str(input("Enter text: "))
        while len(text)==0:
                print("You must enter something to proceed!")
                text=str(input("Enter text: "))
        key=str(input("Enter a key: "))        
        while len(key)== 0:
                print("You must enter a key!")
                key=str(input("Enter a key: "))
##-------------------------------------------------------------------------------------                

def keylen():       ##cuts or repeats the key to decrease or increase the length of key to make it equal to the length of input text or cipher
        global text
        global key
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
##--------------------------------------------------------------------------------------
                
def alph(x):  ## shifts 'al' by x positions		
		global al
		
		if x<=len(al) and x>-1:
			res=[]
			for item in range(len(al)-x):
				res.append(al[item+x])
			
			for item in range(x):
				res.append(al[item-len(al)])

			return res
		else:
			raise ValueError("Parameter for alph must be >-1 and <"+str(len(al)+1))
##---------------------------------------------------------------------------------------

alphmat=[]
for num in range(len(al)):
	alphmat.append(alph(num))				
##---------------------------------------------------------------------------------------
	
def footer():
	print ("")
	print ("Thank you for using Encryo v2.0")
	print("")
##---------------------------------------------------------------------------------------
	
def enc(): ## The encrypter function
	## takes key as input and prints the Vignere cipher as output
	## Uses Vignere cipher to encrypt the text
	## You must see Wikipedia page for Vignere cipher to understand the encryption
	


	getinp()

	global text
	global key
	keylen()
	enc=""
	num1=[]
	num2=[]

	for i in range(len(text)):
		for j in range(len(alphmat[0])):
			if alphmat[0][j] == text[i]:
				num1.append(j)



	for k in range(len(key)):
		for l in range(len(alphmat[0])):
			if alphmat[0][l] == key[k]:
				num2.append(l)


	for n in range(len(num1)):
		enc+=alphmat[num1[n]][num2[n]]			


	print ("")

	print("Encrypted cypher: "+ enc)
	print ("")
##-----------------------------------------------------------------------------------

def dec():  ##The decrypter function
	global text
	global key

	getinp()

	keylen()

				

	dec=""

	num1=[]
	num2=[]

	for j in range(len(key)):
		for i in range(len(alphmat)):
			if alphmat[i][0]==key[j]:
				num1.append(i)

	for j in range(len(text)):
		for i in range(len(alphmat[0])):
			if text[j]==alphmat[num1[j]][i]:
				num2.append(i)

			

	for n in range(len(num2)):
		dec=dec+alphmat[0][num2[n]]

	print ("")

	print("Decrypted text: "+dec)
	print ("")
##----------------------------------------------------------------------------------------------

def menu():	 
        print("Menu: ")
        print("--------------------")
        print("[1] Encrypt a text")
        print("[2] Decrypt a text")
        print("[3] License")
        print("[4] Exit")
        print("")

        inp=str(input("Your response: "))
        print ("")

        if inp=="1":
                enc()
        elif inp=="2":
                dec()
        elif inp=="3":
                gnugpl()
                print("")
        elif inp=="4":
                quit()
        else:
                print("Invalid response. Try again. Enter option # only.")
                print("")
                menu()
##-----------------------------------------------------------------------------------------------

##Final call to functions to start the program

header()
while True:           ##The infinite loop. Keeps showing main menu until exit option is chosen
        menu() 
footer()		    		
##----------------------------------------------------------------------------------------------
