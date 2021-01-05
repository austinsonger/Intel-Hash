"""
    Title:      IntelHash
    Desc:       Takes a Onion URL and Hashes it and compares it against blacklisted hashed onion URLS
    Author:     Austin Songer
    Version:    0.0.1
    GitHub URL: https://github.com/austinsonger/intel-hash
"""


import base64
from unfurl import core
import hashlib
import html.parser
import re
import json
import time
import os
import socket
import strictyaml
import urllib.parse
import requests
from ipwhois import IPWhois
import tkinter
import tkinter.filedialog


from Modules import FileOpen
from datetime import datetime, date

linksFoundList = []
linksRatingList = []
linksSanitized = []
linksDict = {}


def switchMenu(choice):
    if choice == '1':
        hashMenu()
    if choice == '0':
        exit()
    else:
        mainMenu()


def hashSwitch(choice):
    if choice == '1':
        hashOnion()
    if choice == '0':
        mainMenu()


def titleLogo():
    FileOpen.fileOpen()
    os.system('cls||clear')


def mainMenu():
    print("\n --------------------------------- ")
    print("\n              IntelHash            ")
    print("\n --------------------------------- ")
    print(" What would you like to do? ")
    print("\n OPTION 1: Hashing ")
    print(" OPTION 0: Exit Tool")
    switchMenu(input())


def hashMenu():
    print("\n -------------------------------")
    print("             Hashing              ")
    print(" ---------------------------------")
    print(" What would you like to do? ")
    print(" OPTION 1: Enter Onion URL and Hash it")
    print(" OPTION 0: Exit to Main Menu")
    hashSwitch(input())


def hashOnion():
    userinput = input(" Enter the URL to be hashed: ")
    print(" MD5 Hash: " + hashlib.md5(userinput.encode("utf-8")).hexdigest())
    hashMenu()





if __name__ == '__main__':
    titleLogo()
    mainMenu()

