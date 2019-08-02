import subprocess
import pyttsx3

from redis import Redis
from rq import Queue

class Handler:

    def __init__(self):
        self.q = Queue(connection=Redis())

    def status(self, data, enabled):
        if enabled:
            sentences = []
            print("Handle status")
            if data["context"] != "continuous-integration/travis-ci/push":
                # Prevent duplicate announcements.
                return

            author = data["commit"]["commit"]["author"]["name"]

            if data["state"] == "failure":
                message = data["commit"]["commit"]["message"]

                sentences.append("Oh deary me")
                sentences.append(author)
                sentences.append("You broke the build - you bastard - with the commit:")
                sentences.append(message)

            if data["state"] == "success":
                sentences.append("Well done")
                sentences.append(author)
                sentences.append("Good jorb. You fixed it. You fixed the build - I hope you learnt your lesson")

            self.batch_say_sentences(sentences)

    def star(self, data, enabled):
        if enabled:
            sentences = []
            print("Handle star")
            if data["action"] == "created":
                sentences.append("Hey Chris!")
                sentences.append("Well done.")
                sentences.append("Someone just starred your repo named " + data["repository"]["name"])
            if data["action"] == "deleted":
                sentences.append("Oh sorry Chris, They just red the code and decided to unstar it. Sad face")
            
            self.batch_say_sentences(sentences)

    def pull_request_review_comment(self, data, enabled):
        if enabled:
            sentences = []
            print("Handle pull_request_review_comment")
            if data["action"] == "created":
                sentences.append("A new comment was added to your pull request by " + data["comment"]["user"]["login"])
                sentences.append(data["comment"]["body"])
            self.batch_say_sentences(sentences)

    def push(self, data, enabled):
        if enabled:
            sentences = []
            print("Handle Push")
            sentences.append("new commits were pushed to branch" + data["ref"] )
            for commit in data["commits"]:
                sentences.append(commit["message"])
                sentences.append("By " + commit["author"]["name"])

            sentences.append("Oh well I better try and build this shit.")
            sentences.append("Here goes nothing dot dot dot")

            self.batch_say_sentences(sentences)

    def batch_say_sentences(self, sentences):
        self.q.enqueue(text_to_speech, sentences)

def text_to_speech(sentences):
    engine = pyttsx3.init()
    for sentence in sentences:
        print(sentence)
        engine.say(sentence)
    engine.runAndWait()
    return True