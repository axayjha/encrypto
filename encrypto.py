## <AXAY/>
## <akshayjha@live.in>
## <fb.com/AxayJha>

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
        print("[3] Exit")
        print("")

        inp=str(input("Your response: "))
        print ("")

        if inp=="1":
                enc()
        elif inp=="2":
                dec()
        elif inp=="3":
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
