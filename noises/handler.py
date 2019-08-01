from noises.threader import Threader

from subprocess import call
import subprocess

import json


class Handler:

    def status(self, data, enabled):
        if enabled:
            print(json.dumps(data))
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

            if data["state"] == "pending":
                wordsQueue.append("Oh look some new code by " + author)
                wordsQueue.append("I hope you know what you're doing dot dot dot")
                wordsQueue.append("Oh well I better try and build this shit. Hold onto your butts")

            speakWords(wordsQueue)

    def star(self, data, enabled):
        if enabled:
            print(json.dumps(data))
            wordsQueue = []
            if data["action"] == "created":
                wordsQueue.append("Hey Chris")
                wordsQueue.append("Well done. Someone just starred your repo named " + data["repository"]["name"])
            if data["action"] == "deleted":
                wordsQueue.append("Oh sorry Chris, They just red the code and decided to unstar it. Sad face")

            speakWords(wordsQueue)

    def pull_request_review_comment(self, data, enabled):
        if enabled:
            print(json.dumps(data))
            wordsQueue = []
            if data["action"] == "created":
                wordsQueue.append("A new comment was added to your pull request by " + data["comment"]["user"]["login"])
                wordsQueue.append(data["comment"]["body"])

            speakWords(wordsQueue)

def speakWords(wordsQueue):
    haha = ". ".join(str(x) for x in wordsQueue)
    subprocess.Popen(["python3", "./noises/speak.py", haha])