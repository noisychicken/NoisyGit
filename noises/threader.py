import pyttsx3
from threading import Thread

class Threader(Thread):
    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.daemon = True
        self.start()
        self.tts_engine = pyttsx3.init()

    def queueWords(self, words):
        self.tts_engine.say(self._args)

    def speak(self):
        self.tts_engine.runAndWait()
