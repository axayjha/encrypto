## Author: <AXAY/>
## <akshayjha@live.in>
## <github.com/axayjha>
## <www.akshayjha.co.nr>

## Under GNU LGPL v3.0 License.
## Free to use, modify and distribute! 

##_________________________________________________________________________________
        

global ALL_KEYS     
global ALPHA_MATRIX  ##the 96 * 96 matrix of all possible inputs (ALL_KEYS)

##----------------------------------------------------------------------------------

SMALL_ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m'\
,'n','o','p','q','r','s','t','u','v','w','x','y','z']

CAP_ALPHA   = ['A','B','C','D','E','F','G','H','I','J','K','L','M'\
,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

NUMBERS     = ['1','2','3','4','5','6','7','8','9','0']

OTH_KEYS    = [' ','`','~','!','@','#','$','%','^','&','*','(',')','-',\
'_','=','+','[','{',']','}','\\','|',';',':','\'','\"',',','<','.','>','/','?',']',]

ALL_KEYS = SMALL_ALPHA + CAP_ALPHA + NUMBERS + OTH_KEYS  
##list of all inputs possible from a 96 key keyboard

##-----------------------------------------------------------------------------------

def header():
	print("")
	print ("+===============================================================+")
	print ("|                                                               |")
	print ("|                                                               |")
	print ("|               --- Welcome to Encrypto v0.6 ---                |")
	print ("|                                                               |")
	print ("|                                                        //AXAY |")
	print ("+===============================================================+")
	print("")


##------------------------------------------------------------------------------------

def getText():
        try:
          print("Enter text")
          usr_Buff = str(input("> "))
        except:
          TypeError or ValueError ("Enter a valid text. Try again.")
          getText()

        while len(usr_Buff)==0:
                print("You must enter something to proceed! Try again.")
                usr_Buff=str(input("> "))
        print("")
        return usr_Buff


##-------------------------------------------------------------------------------------                

def getKey(usr_Buff):       
        """Gets key and cuts or repeats the key to decrease or increase the length of key 
        to make it equal to the length of input text or cipher"""

        try:
          print("Enter key")
          key=str(input("> "))
        except:
          TypeError or ValueError ("Enter a valid key. Try again.")
          getKey(usr_Buff)

        while len(key)== 0:
                print("You must enter a key! Try again.")
                key=str(input("> "))
        print("")

        if len(key)<len(usr_Buff):
                temp=key                
                i=0
                while len(temp)<len(usr_Buff):
                        temp=temp+key[(i%len(key))]
                        i=i+1
                key=temp
                        
        elif len(key)>len(usr_Buff):
                temp=""
                for i in range(len(usr_Buff)):
                        temp=temp+key[(i%len(key))]
                key=temp
        
        return key

##--------------------------------------------------------------------------------------
                
def alphaShift(x): 
  global ALL_KEYS

  if x<=len(ALL_KEYS) and x>-1:
  	res=[]
  	for ITER in range(len(ALL_KEYS)-x):
  		res.append(ALL_KEYS[ITER+x])
  	
  	for ITER in range(x):
  		res.append(ALL_KEYS[ITER-len(ALL_KEYS)])

  	return res

  else:
  	raise ValueError("Parameter for alphaShift must be >-1 and <"+str(len(ALL_KEYS)+1))

##---------------------------------------------------------------------------------------

ALPHA_MATRIX = []

for MOD in range(len(ALL_KEYS)):
	ALPHA_MATRIX.append(alphaShift(MOD))		


##---------------------------------------------------------------------------------------
	
def encrypt(text, key): 

	CIPHER=""

	ZENER_SWAP=[]
	BUFFER_SWAP=[]

	for i in range(len(text)):
		for j in range(len(ALPHA_MATRIX[0])):
			if ALPHA_MATRIX[0][j] == text[i]:
				ZENER_SWAP.append(j)



	for k in range(len(key)):
		for l in range(len(ALPHA_MATRIX[0])):
			if ALPHA_MATRIX[0][l] == key[k]:
				BUFFER_SWAP.append(l)


	for n in range(len(ZENER_SWAP)):
		CIPHER += ALPHA_MATRIX[ZENER_SWAP[n]][BUFFER_SWAP[n]]			


	return CIPHER
##-----------------------------------------------------------------------------------

def decrypt(cipher, key):  
	DEC_CIPHER=""

	ZENER_SWAP=[]
	BUFFER_SWAP=[]

	for j in range(len(key)):
		for i in range(len(ALPHA_MATRIX)):
			if ALPHA_MATRIX[i][0] == key[j]:
				ZENER_SWAP.append(i)

	for j in range(len(cipher)):
		for i in range(len(ALPHA_MATRIX[0])):
			if cipher[j] == ALPHA_MATRIX[ZENER_SWAP[j]][i]:
				BUFFER_SWAP.append(i)

			

	for n in range(len(BUFFER_SWAP)):
		DEC_CIPHER += ALPHA_MATRIX[0][BUFFER_SWAP[n]]

	return DEC_CIPHER
##----------------------------------------------------------------------------------------------

def main():	 
        print("Menu: ")
        print("--------------------")
        print("[1] Encrypt a text")
        print("[2] Decrypt a cipher")
        print("[3] Exit")
        print("")

        usr_Buff=str(input("Your response > "))

        print ("")

        if usr_Buff=="1":
                text = getText()
                key = getKey(text)
                print("Encrypted cipher: "+ encrypt(text, key))
                print("")

        elif usr_Buff=="2":
                text = getText()
                key = getKey(text)
                print("Decrypted text: " + decrypt(text, key))
                print("")

        elif usr_Buff=="3":
                print("Bye!")
                print("")
                quit()
                
        else:
                print("Invalid response. Try again. Enter option # only.")
                print("")
                main()
##-----------------------------------------------------------------------------------------------

##Final call to functions to start the program

header()
while True:           ##The infinite loop. Keeps showing main menu until exit option is chosen
        main()        
	    		
##----------------------------------------------------------------------------------------------
