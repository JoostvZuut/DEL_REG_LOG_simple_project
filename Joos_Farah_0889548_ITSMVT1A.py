import hashlib
from easygui import *
import easygui
from pathlib import Path

username= ''
password= ''

def mainmenu():
    msg = ("Selecteer uw keuze")
    title = "Opties menu"
    choices = [ "Inloggen", "Registreren", "Gebruiker verwijderen"]
    choice = easygui.choicebox(msg, title, choices)
    print(choice)
    if choice == "Inloggen":
        loginscreen()
    elif choice == "Registreren":
        registratiescreen()
    elif choice == "Gebruiker verwijderen":
        deleteuser()

def registratiescreen():
    msg= "Registreer"
    title= "Registratieformulier"
    fieldNames= ['Gebruikersnaam', 'Wachtwoord']
    fieldValues= []
    fieldValues= multpasswordbox(msg, title, fieldNames)
    if fieldValues == None:
        mainmenu()

    username= fieldValues[0]
    password= fieldValues[1]

    hashedpw= hashlib.sha1(password.encode("utf-8")).hexdigest()
    f= open("userpass.txt", "a+")
    f.write('\n')
    f.write(username)
    f.write(hashedpw)
    f.close()
    registratiescreen()


def loginscreen():
    msg= "Login met uw gebruikersnaam en wachtwoord"
    title= "Loginscherm"
    fieldNames= ['Gebrukersnaam', 'Wachtwoord']
    fieldValues= []
    fieldValues= easygui.multpasswordbox(msg, title, fieldNames)
    if fieldValues == None:
        mainmenu()
    usernameAttempt = fieldValues[0]
    passwordAttempt= fieldValues[1]
    hashedpwAttempt= hashlib.sha1(passwordAttempt.encode('utf-8')).hexdigest()

    with open("userpass.txt") as myfile:
        if usernameAttempt and hashedpwAttempt in myfile.read():
            easygui.msgbox('Welkom, u bent ingelogd')
            loginscreen()
        else:
            easygui.msgbox("Gebruikersnaam of wachtwoord is onjuist.")
            loginscreen()

    print(fieldValues)

def deleteuser():
    msg= 'Type de gebruikersnaam van de gebruiker die u wenst te verwijderen.'
    title= "Gebruiker verwijderen"
    fieldNames= [""]
    fieldValues= []
    fieldValues= easygui.enterbox(msg, title, fieldNames)
    if fieldValues == None:
        mainmenu()

    myfile = open(userpass.txt, "rt")
    data= myfile.read()
    data= data.replace(usernametoDelete, 'null')
    myfile.close()
    myfile= open("userpass.txt", 'wt')
    myfile.write(data)
    myfile.close()
    easygui.msgbox("Gebruiker verwijderd.")
    mainmenu()


mainmenu()
