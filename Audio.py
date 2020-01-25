import os
import pyttsx3

engine = pyttsx3.init()

def speed_audio(speed):
    global engine
    engine.say("speed is {0}.".format(speed))
    engine.runAndWait()

def heel_strike_audio():
    os.system('mpg321 heel_striking.mp3')

def increase_tilt_audio():
    os.system('mpg321 increase_tilt.mp3')

def decrease_tilt_audio():
    os.system('mpg321 decrease_tilt.mp3')

def cadence_audio():
    os.system('mpg321 cadence.mp3')

def overstriding_audio():
    os.system('mpg321 overstriding2.mp3')