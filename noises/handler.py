import pyttsx3

from noises.threader import Threader


class Handler:

    def status(self, data, enabled):
        if enabled:
            threader = Threader(args=None)

            engine = pyttsx3.init()
            author = data["commit"]["commit"]["author"]["name"]

            if data["state"] == "failure":
                message = data["commit"]["commit"]["message"]

                threader.queueWords("Oh deary me")
                threader.queueWords(author)
                threader.queueWords("You broke the build - you bastard - with the commit:")
                threader.queueWords(message)
                threader.speak()

            if data["state"] == "success":
                threader.queueWords("Well done")
                threader.queueWords(author)
                threader.queueWords("Good jorb. You fixed it. You fixed the build - I hope you learnt your lesson")
                threader.speak()