import pyttsx3
from threading import Thread

# Threading Class
class Threader(Thread):
    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.daemon = True
        self.start()

    def run(self):
        tts_engine = pyttsx3.init()
        tts_engine.say(self._args)
        tts_engine.runAndWait()
