# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 08:29:10 2021

@author: TREAF ALSHEMERI
"""

import requests 
from tkinter import *

api_key = "Here's your API Key from Cuttly"

#This function is callback for Submit button
def submitClicked(self):
    #Check if Entry is empty
    if len(textField.get()) > 0:
        url = textField.get() # get the url from Entry
        api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}" # Passing the api key and url
        data = requests.get(api_url).json()["url"] 
        if data["status"] == 7: # If everything is ok then get the shorter link
            shortened_url = data["shortLink"]
            urlLabel.config(text=shortened_url) # change label text to the shorter link
        else:
            print("Error Shortening URL:", data) # Error Message

# This is callback for copy button from label 
def copyFromLabel(self):
    url = urlLabel.cget("text") # Get the text from label
    window.clipboard_append (url) # Add it to the clipboard
    
window = Tk() # Create new Window
textField = Entry(window , text = "Enter your link" , bd = 2) # Create Entry or TextField
textField.place(width= 300 , height = 30 , x = 30 , y = 30) # Position the TextField
submitBtn = Button(window , text= "Submit" , fg = 'black') # Create Submit Button
submitBtn.place(x= 340 , y= 30) # Position the submit Button
submitBtn.bind('<Button-1>' , submitClicked) # Event For Submit Button
copyBtn = Button(window , text = "Copy" , fg = 'black') #Create Copy Button
copyBtn.place(x=180 , y=70) # Position the copy Button
copyBtn.bind('<Button-1>' , copyFromLabel) #Event for Copy Button
urlLabel = Label(window , text="Here's your shortner link" , fg='red') #Create label
urlLabel.place(x=30 , y = 70) #Position the label
window.title("URL Shortener") # Window's Title
window.geometry("400x300+10+10") # Size of the window
window.mainloop() # Make the window appears 


