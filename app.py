
import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Meta AI Agent is running successfully!", 200

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if verify_token == "my_secure_token":
            return challenge, 200
        return "Verification token mismatch", 403
    elif request.method == "POST":
        data = request.get_json(silent=True)
        print(">>> WEBHOOK POST RECEIVED:", data)
        return "EVENT_RECEIVED", 200

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
