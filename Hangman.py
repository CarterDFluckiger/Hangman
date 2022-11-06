import random
import time

#These have to do with importing the pictures
import io
import os

import PySimpleGUI as sg

import PIL
from PIL import Image


#Got this working in Test.py
image = Image.open(r'C:\Users\carte\OneDrive\Desktop\Coding\Hangman\HM_1.png')
image.thumbnail((200, 200))
bio = io.BytesIO()
image.save(bio, format="PNG")

    
sg.theme ( 'DarkPurple' )

layout =[   [sg.Image( key="-IMAGE-")],
            [sg.Text(('')), sg.Text(size=(50,1), key='-OUTPUT-')],    
            [sg.Input(key='-IN-')],
            [sg.Button("ENTER"), sg.Exit("EXIT GAME")]]

gamelayout =[ [sg.Image(data=bio.getvalue(), key="-IMAGE-")],
              [sg.Text("Welcome to the Game"), sg.Text(size=(15,1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Button(), sg.Exit("EXIT GAME")]]
               

window = sg.Window("Hangman Game", layout, margins = (400, 200),finalize=True, resizable = True)
window['-OUTPUT-'].update('Hello, please enter a word or phrase for the Hangman Game')


#Opens the window and asks for a sentence to play hangman
def StartGame():
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
                print('Invalid Entry')
            #Need this to not get errror is the length is zero
            else:
                #Have to do this after making sure the length isnt' zero
                last_char = inputString[-1]
                if ( last_char == ' '):
                    print ( "Invalid Entry - Ends with a Space" )
                else:
                    print('Valid')
                    PlayGame(values['-IN-'])
                    valid = True
                

        if event == sg.WIN_CLOSED or event =='EXIT GAME':
            break

def PlayGame(inputString):
    print ( inputString )
    
    #Refreshing the screen to the game screen
    Refresh( "Game" )
    #Maybe create another function for the actual game.
    #Probalby pass - InputString,
    
    


#Checks if the input has numbers in ( we don't want numbers in their)
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

#Now it will update the text.
#Needs to update the text box to get rid of it
#Needs to input my picture
def Refresh( ScreenType ):

    if ( ScreenType == "Game" ):
        
        #HOLY FUCK I DID IT
        window['-IMAGE-'].update(data=bio.getvalue())
        window['-OUTPUT-'].update(("Now you play the game"))
        event , values = window.read()
        
    else:
        print("else")


StartGame()
print( "Window Closed")
window.close()
