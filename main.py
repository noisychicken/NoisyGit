import pyttsx3
from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))
    engine.say("Something happened")
    engine.runAndWait()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    engine = pyttsx3.init()
