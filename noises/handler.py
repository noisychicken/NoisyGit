import pyttsx3

from noises.threader import Threader


class Handler:

    def status(self, data, enabled):
        if enabled:
            engine = pyttsx3.init()
            author = data["commit"]["commit"]["author"]["name"]
            wordsQueue = []

            if data["state"] == "failure":
                message = data["commit"]["commit"]["message"]

                wordsQueue.append("Oh deary me")
                wordsQueue.append(author)
                wordsQueue.append("You broke the build - you bastard - with the commit:")
                wordsQueue.append(message)

            if data["state"] == "success":
                wordsQueue.append("Well done")
                wordsQueue.append(author)
                wordsQueue.append("Good jorb. You fixed it. You fixed the build - I hope you learnt your lesson")

            my_thread = Threader(args=wordsQueue)


