
from github_webhook import Webhook
from flask import Flask
from noises.handler import Handler

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint
handlers = Handler()


@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"


@webhook.hook(event_type="status")        # Defines a handler for the 'push' event
def on_status(data):
    handlers.status(data, True)

@webhook.hook(event_type="star")
def on_star(data):
    handlers.star(data, True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
