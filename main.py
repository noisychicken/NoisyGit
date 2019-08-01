import pyttsx3
from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook(event_type="status")        # Defines a handler for the 'push' event
def on_status(data):
    print("Got status with: {0}".format(data))
    engine = pyttsx3.init()

    if data["state"] == "failure":
        description = data["description"]
        author = data["commit"]["commit"]["author"]["name"]

        print(description)
        print(author)

        engine.say("Oh noes")
        engine.say(author)
        engine.say("You broke the build sadface dot jpeg")
        engine.say(description)
        engine.runAndWait()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
