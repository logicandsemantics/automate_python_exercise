#!/usr/bin/env python3
# Project: mapit.py with the webbrowser Module
import webbrowser, sys, pyperclip

# webbrowser.open('http://thelowry.com')

# this code will open the map and find the location you type in or copied in clipboard already
sys.argv

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
