import sys
import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    return engine

def say(words):
    for word in words.split("MARKER"):
        engine.say(word)
    engine.runAndWait() #blocks

engine = init_engine()
say(str(sys.argv[1]))