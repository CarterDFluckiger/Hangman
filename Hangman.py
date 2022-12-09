import random
import time

#These have to do with importing the pictures
import io
import os

import PySimpleGUI as sg

import PIL
from PIL import Image




n = 49

image = Image.open(r'C:\Users\carte\OneDrive\Desktop\Coding\Hangman\HM_' + chr(n) + '.png')
image.thumbnail((200, 200))
bio = io.BytesIO()
image.save(bio, format="PNG")

    
sg.theme ( 'DarkPurple' )

layout =[   [sg.Image( key="-IMAGE-")],
            [sg.Text(('')), sg.Text(size=(50,1), key='-OUTPUT-')],
            [sg.Text(('')), sg.Text(size=(50,1), key='-OUTPUT2-')],
            [sg.Text(('')), sg.Text(size=(50,1), key='-OUTPUT3-')],
            [sg.Input(key='-IN-', do_not_clear=False)],
            [sg.Button("ENTER"), sg.Exit("EXIT GAME")]]

window = sg.Window("Hangman Game", layout, margins = (150, 150),finalize=True, resizable = True)
window['-OUTPUT-'].update('Hello, please enter a word or phrase for the Hangman Game')


#Opens the window and asks for an input to play hangman
def getInput():
    valid = False
    values = ""
    length = 0
    
    
    while valid == False:
        event , values = window.read()

        #Rechecks everything after every press of enter
        if event == "ENTER":
            #Checks length everytime it loops
            length = len(values['-IN-'])

            inputString = values['-IN-']
            
            if (length == 0 or (has_numbers(values['-IN-']) == True)):
                #
                #Delete this at the end
                print('Invalid Entry')
                window['-OUTPUT2-'].update('Invalid Entry - No Input')
            #Need this to not get errror is the length is zero
            else:
                #Have to do this after making sure the length isnt' zero
                last_char = inputString[-1]
                if ( last_char == ' '):
                    #
                    #Delete this at the end
                    print ( "Invalid Entry - Ends with a Space" )
                    window['-OUTPUT2-'].update('Invalid Entry - Ends with a Space')
                else:
                    print('Valid Entry')
                    window['-OUTPUT2-'].update('')
                    PlayGame(values['-IN-'])
                    valid = True
                

        if event == sg.WIN_CLOSED or event =='EXIT GAME':
            break

def PlayGame(inputString):
    x = 0
    correctGuesses = 0
    #Refreshing the screen to the game screen
    Refresh( n )
    
    arr = list(inputString)
    arrGuessed = []

    correctGuesses = numSpaces(arr)

    root = arrayToList(arr, len(arr))
    String = update(root)
    window['-OUTPUT2-'].update(String)

    #Guessing Loop
    #There isn't a do while. Might have to do while(True) and break statement with the Gamewon() function
    while(correctGuesses != len(arr)):
        x = 0
        event , values = window.read()
        inVal = values['-IN-']

        guessed = alreadyGuessed(arrGuessed, inVal )

        if(event == sg.WIN_CLOSED or event =='EXIT GAME'):
            break

        elif( n == 55 ):
            newImage(n)
            GameLost(inputString)
            return 0
        
        elif( len(inVal) == 1 and (inVal.isdigit() == False and guessed == False)):
            arrGuessed.append(inVal)
            print(alreadyGuessed)
            print("Valid Input")
            root, x  = CheckGuess( inVal, root )
            
            if(x == 0):
                print("Incorrect Guess")
                newImage(n)
            
            window['-OUTPUT2-'].update(update(root))
            correctGuesses = correctGuesses + x
        else:
            print( "Invalid" )
    if(correctGuesses == len(arr)):
        #window['-Image-'].update("")
        window['-OUTPUT-'].update("You won the Game!")
        window['-OUTPUT2-'].update("The answer was: "+ inputString)
        window['-OUTPUT3-'].update("")
        event , values = window.read()
        event , values = window.read()
    


def newImage(i):
    global n
    print( n )
    n +=1
    image = Image.open(r'C:\Users\carte\OneDrive\Desktop\Coding\Hangman\HM_' + chr(n) + '.png')
    image.thumbnail((200, 200))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    
    window['-IMAGE-'].update(data=bio.getvalue())

    
def alreadyGuessed(arr, char):
    for x in arr:
        if(x == char):
            return True
    return False


#Checks if the input has numbers in ( we don't want numbers in their)
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

#Now it will update the text.
#Needs to update the text box to get rid of it
#Needs to input my picture
def Refresh( a ):

        #HOLY FUCK I DID IT
        window['-IMAGE-'].update(data=bio.getvalue())
        window['-OUTPUT-'].update(("Please Enter a letter to guess"))

def GameLost(inputString):
        window['-OUTPUT-'].update("You fucking lost the Game!")
        window['-OUTPUT2-'].update("The answer was: "+ inputString)
        window['-OUTPUT3-'].update("You suck")
        event , values = window.read()

def playAgain():
    global n
    n = 49

#---------------------------------------------------------------------
#--------Input, Node, Checkguess, New Image Functions-----------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

# Representation of a node
class Node: 
    def __init__(self, val, show = False): 
        self.val = val
        self.next = None
        self.show = False
  
# Function to insert node
def insert(root, item):
    temp = Node(item)

    if(item == ' '):
        temp.show = True
    else:
        temp.show = False
      
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
      
    return root
  
def update(root):
    Str = ""
    
    while (root != None):
        if( root.show == True ):
            if(root.val == " "):
                Str = Str + "       " + root.val
            else:
                Str = Str + " " + root.val
        else:
            Str = Str + " _ "
        root = root.next

    return Str
          
def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
      
    return root

#Finds the number of spaces in the array of characters
def numSpaces(arr):
    p = 0
    for x in arr:
        if(arr[x] == ' '):
            p += 1
    return p

def CheckGuess( char, head ):
    curr = head
    n = 0
    while( curr != None ):
        if( curr.val == char or curr.val == char.upper() or curr.val == char.lower() ):
            if( curr.show == False ):
                n = n + 1
            curr.show = True
            curr = curr.next
        else:
            curr = curr.next
    print( "You found ", n ," instances of -" , char , "-" )

    return head, n

def numSpaces(array):
    p = 0
    for x in array:
        if(x == ' '):
            p += 1
    return p


getInput()
print( "Window Closed")
window.close()
