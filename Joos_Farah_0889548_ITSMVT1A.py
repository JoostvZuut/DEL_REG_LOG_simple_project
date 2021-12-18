import hashlib
from easygui import *
import easygui
from pathlib import Path

username= ''
password= ''

if easygui.ccbox(msg="Welkom op onze platform", title="Startscherm"):
     pass
else:
     quit()

def mainmenu():
    msg = ("Selecteer uw keuze")
    title = "Hoofdmenu"
    choices = [ "Inloggen", "Registreren", "Gebruiker verwijderen"]
    choice = easygui.choicebox(msg, title, choices)
    print(choice)
    if choice == "Inloggen":
        loginscherm()
    elif choice == "Registreren":
        registratiescherm()
    elif choice == "Gebruiker verwijderen":
        verwijdergebruikerscherm()

def registratiescherm():
    msg= "Registreer"
    title= "Registratieformulier"
    fieldNames= ['Gebruikersnaam', 'Wachtwoord']
    fieldValues= []
    fieldValues= easygui.multpasswordbox(msg, title, fieldNames)
    if fieldValues == None:
        mainmenu()

    username= fieldValues[0]
    password= fieldValues[1]

    hashedpw= hashlib.sha1(password.encode("utf-8")).hexdigest()
    f= open("userinfo.txt", "a+")
    f.write('\n')
    f.write(username)
    f.write(hashedpw)
    easygui.ccbox(msg="Bedankt voor uw registratie, u kunt nu inloggen.", title= "Registratie")
    mainmenu()


def loginscherm():
    msg= "U kunt inloggen met uw gebruikersnaam en wachtwoord"
    title= "Loginscherm"
    fieldNames= ['Gebruikersnaam', 'Wachtwoord']
    fieldValues= []
    fieldValues= easygui.multpasswordbox(msg, title, fieldNames)
    if fieldValues == None:
        mainmenu()
    usernameAttempt= fieldValues[0]
    passwordAttempt= fieldValues[1]
    hashedpwAttempt= hashlib.sha1(passwordAttempt.encode('utf-8')).hexdigest()

    with open("userinfo.txt") as myfile:
        if usernameAttempt and hashedpwAttempt in myfile.read():
            easygui.msgbox("Welkom u bent ingelogd.", ok_button= "Beëindigen")
            loginscreen()
        else:
            easygui.msgbox("Gebruikersnaam of wachtwoord is onjuist.")
            loginscreen()
    mainmenu()


def verwijdergebruikerscherm():
    msg= 'Type de gebruikersnaam van de gebruiker die u wenst te verwijderen.'
    title= "Gebruiker verwijderen"
    fieldNames= [""]
    fieldValues= []
    fieldValues= easygui.enterbox(msg, title, fieldNames)
    if fieldValues == None:
        mainmenu()

    with open("userinfo.txt") as myfile:
        if username in myfile.read():
        myfile = open(userinfo.txt, "rt")
        data= myfile.read()
        data= data.replace(usernametoDelete, 'null')
        myfile.close()
        myfile= open("userinfo.txt", 'wt')
        myfile.write(data)
        myfile.close()
        easygui.msgbox("Gebruiker is succesvol verwijderd.")
        mainmenu()


mainmenu()
