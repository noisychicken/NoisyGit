import pyttsx3


class Handler:

    def status(self, data, enabled):
        if enabled:
            engine = pyttsx3.init()
            author = data["commit"]["commit"]["author"]["name"]

            if data["state"] == "failure":
                message = data["commit"]["commit"]["message"]

                engine.say("Oh deary me")
                engine.say(author)
                engine.say("You broke the build - you bastard - with the commit:")
                engine.say(message)

                engine.runAndWait()
                engine.stop()

            if data["state"] == "success":
                engine.say("Well done")
                engine.say(author)
                engine.say("Good jorb. You fixed it. You fixed the build - I hope you learnt your lesson")

                engine.runAndWait()
                engine.stop()
