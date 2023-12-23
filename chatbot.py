
import google.generativeai as genai
import tkinter as tk
from tkinter import *

import os

genai.configure(api_key="AIzaSyCqJpJ-KADaNEGw0Y7L3zvk_MCut-lwZI4")
model = genai.GenerativeModel('gemini-pro')

def generate():
  message = message_entry.get()
  if message:
    message_history.config(state=tk.NORMAL)
    message_history.insert(tk.END, f"You: {message}\n\n")
    response = model.generate_content(message)
    message_history.insert(tk.END, f"Bot: {response.text}\n\n")
    message_history.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)

def clear():
  message_history.config(state=tk.NORMAL)
  message_history.config(text="")
  message_history.config(state=tk.DISABLED)


# Create the main window
parent = tk.Tk()
parent.title("ChatBot")

# Create a Text widget for message history
message_history = tk.Text(parent, wrap=tk.WORD)
message_history.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
message_history.config(state=tk.DISABLED)

# Create an Entry widget for entering messages
message_entry = tk.Entry(parent, width=50)
message_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a "Send" button
send_button = tk.Button(parent, text="Generate", command=generate, width=20, bg="Green", fg="White")
send_button.grid(row=1, column=1, padx=10, pady=10)

# Create a "Clear" button
clear_button = tk.Button(parent, text="Clear", command=clear, width=20)
clear_button.grid(row=1, column=2, padx=10, pady=10)

# Start the Tkinter event loop
parent.mainloop()
