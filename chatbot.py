import google.generativeai as genai
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import pyttsx3

import os

# Configure and the set the API Key
genai.configure(api_key="GOOGLE_API_KEY")

# Define the model
model = genai.GenerativeModel('gemini-pro')

# Initialize the recognizer 
recognizer = sr.Recognizer() 

def SpeakText(command):
  # Initialize the engine
  engine = pyttsx3.init()
  engine.say(command) 
  engine.runAndWait()

def TextToSpeech():
  try:
    if len(response.text)<=100:
      SpeakText(response.text)
    else:
      tkinter.messagebox.showinfo(title=None, message="Response Too Long")
  except:
    tkinter.messagebox.showinfo(title=None, message="Error Occured")

def generate():
  message = message_entry.get()
  if message:
    message_history.config(state=tk.NORMAL)
    message_history.insert(tk.END, f"You: {message}\n\n")
    global response
    response = model.generate_content(message)
    message_history.insert(tk.END, f"Bot: {response.text}\n\n")
    message_history.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)

def clear():
  message_history.config(state=tk.NORMAL)
  message_history.delete("1.0","end")
  message_history.config(state=tk.DISABLED)

   
def SpeechRecognition():
  try: 
      # use the microphone as source for input.
      with sr.Microphone() as source2:
            
          # wait for a second to let the recognizer
          # adjust the energy threshold based on
          # the surrounding noise level 
          recognizer.adjust_for_ambient_noise(source2, duration=0.2)
            
          #listens for the user's input 
          audio2 = recognizer.listen(source2)
            
          # Using google to recognize audio
          MyText = recognizer.recognize_google(audio2)
          MyText = MyText.lower()

          message_entry.insert(tk.END, f"{MyText}")
          SpeakText(MyText)
            
  except sr.RequestError as e:
    tkinter.messagebox.showinfo(title=None, message="Could not request results; {0}".format(e))

  except sr.UnknownValueError:
    tkinter.messagebox.showinfo(title=None, message="unknown error occurred")

def Close():
  parent.destroy()

# Create the main window
parent = tk.Tk()
parent.title("ChatBot")

# Create a Text widget for message history
message_history = tk.Text(parent, wrap=tk.WORD)
message_history.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
message_history.config(state=tk.DISABLED)

# Create a Scrollbar
scroll = tk.Scrollbar(parent, command=message_history.yview)
message_history.configure(yscrollcommand=scroll.set)
scroll.grid(row=0, column=4, padx=10, pady=10)

# Create a Speech to Text button
stt_button = tk.Button(parent, text="Listen", command=SpeechRecognition, width=20, bg="Yellow")
stt_button.grid(row=1, column=0, padx=10, pady=10)

# Create a Text to Speech button
tts_button = tk.Button(parent, text="Speak", command=TextToSpeech, width=20, bg="Yellow")
tts_button.grid(row=1, column=1, padx=10, pady=10)

# Create a Close Button
close_button = tk.Button(parent, text="Close", command=Close, width=20, bg="Red", fg="White")
close_button.grid(row=1, column=2, padx=10, pady=10)

# Create an Entry widget for entering messages
message_entry = tk.Entry(parent, width=50)
message_entry.grid(row=2, column=0, padx=10, pady=10)

# Create a "Send" button
send_button = tk.Button(parent, text="Generate", command=generate, width=20, bg="Green", fg="White")
send_button.grid(row=2, column=1, padx=10, pady=10)

# Create a "Clear" button
clear_button = tk.Button(parent, text="Clear", command=clear, width=20, bg="Light Blue")
clear_button.grid(row=2, column=2, padx=10, pady=10)

# Start the Tkinter event loop
parent.mainloop()
