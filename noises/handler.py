import subprocess
import pyttsx3

from redis import Redis
from rq import Queue

class Handler:

    def __init__(self):
        self.q = Queue(connection=Redis())

    def status(self, data, enabled):
        if enabled:
            print("Handle status")
            if data["context"] != "continuous-integration/travis-ci/push":
                # Prevent duplicate announcements.
                return

            author = data["commit"]["commit"]["author"]["name"]

            if data["state"] == "failure":
                message = data["commit"]["commit"]["message"]

                self.speak_those_words("Oh deary me")
                self.speak_those_words(author)
                self.speak_those_words("You broke the build - you bastard - with the commit:")
                self.speak_those_words(message)

            if data["state"] == "success":
                self.speak_those_words("Well done")
                self.speak_those_words(author)
                self.speak_those_words("Good jorb. You fixed it. You fixed the build - I hope you learnt your lesson")

    def star(self, data, enabled):
        if enabled:
            print("Handle star")
            if data["action"] == "created":
                self.speak_those_words("Hey Chris!")
                self.speak_those_words("Well done.")
                self.speak_those_words("Someone just starred your repo named " + data["repository"]["name"])
            if data["action"] == "deleted":
                self.speak_those_words("Oh sorry Chris, They just red the code and decided to unstar it. Sad face")

    def pull_request_review_comment(self, data, enabled):
        if enabled:
            print("Handle pull_request_review_comment")
            if data["action"] == "created":
                self.speak_those_words("A new comment was added to your pull request by " + data["comment"]["user"]["login"])
                self.speak_those_words(data["comment"]["body"])

    def push(self, data, enabled):
        if enabled:
            print("Handle Push")
            self.speak_those_words("new commits were pushed to branch" + data["ref"] )
            for commit in data["commits"]:
                self.speak_those_words(commit["message"])
                self.speak_those_words("By " + commit["author"]["name"])

            self.speak_those_words("Oh well I better try and build this shit.")
            self.speak_those_words("Here goes nothing dot dot dot")

    def speak_those_words(self, sentence):
        self.q.enqueue(text_to_speech, sentence)


    def speakWords(self, wordsQueue):
        for sentence in wordsQueue:
            self.speak_those_words(sentence)

def text_to_speech(sentence):
    engine = pyttsx3.init()
    print(sentence)
    engine.say(sentence)
    engine.runAndWait()
    return True