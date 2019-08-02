import subprocess


class Handler:

    def status(self, data, enabled):
        if enabled:
            print("Handle status")
            if data["context"] != "continuous-integration/travis-ci/push":
                # Prevent duplicate announcements.
                return

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

            speakWords(wordsQueue)

    def star(self, data, enabled):
        if enabled:
            print("Handle star")
            wordsQueue = []
            if data["action"] == "created":
                wordsQueue.append("Hey Chris!")
                wordsQueue.append("Well done.")
                wordsQueue.append("Someone just starred your repo named " + data["repository"]["name"])
            if data["action"] == "deleted":
                wordsQueue.append("Oh sorry Chris, They just red the code and decided to unstar it. Sad face")

            speakWords(wordsQueue)

    def pull_request_review_comment(self, data, enabled):
        if enabled:
            print("Handle pull_request_review_comment")
            wordsQueue = []
            if data["action"] == "created":
                wordsQueue.append("A new comment was added to your pull request by " + data["comment"]["user"]["login"])
                wordsQueue.append(data["comment"]["body"])

            speakWords(wordsQueue)

    def push(self, data, enabled):
        if enabled:
            print("Handle Push")
            wordsQueue = []
            wordsQueue.append("new commits were pushed to branch" + data["ref"] )
            for commit in data["commits"]:
                wordsQueue.append(commit["message"])
                wordsQueue.append("By " + commit["author"]["name"])

            wordsQueue.append("Oh well I better try and build this shit.")
            wordsQueue.append("Here goes nothing dot dot dot")
            speakWords(wordsQueue)


def speakWords(wordsQueue):
    haha = "MARKER".join(str(x) for x in wordsQueue)
    subprocess.Popen(["python3", "./noises/speak.py", haha])