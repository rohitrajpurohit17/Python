# Install an external module and use it to perform an operation of your interest

# Using external Module
# Here I import pyttsx3 module 
# which covert text into audio

import pyttsx3

engine = pyttsx3.init()
engine.say("Hey! My self Rohit Rajpurohit")
engine.runAndWait()