from flask import Flask, request, jsonify
import hashlib
import hmac
import logging

from config import *
from trigger import run

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():

    signature = request.headers.get("X-Hub-Signature-256")

    body = request.data

    expected = "sha256=" + hmac.new(
        GITHUB_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, expected):
        logging.info("Invalid Signature")
        return jsonify({"message":"Invalid Signature"}),401

    payload = request.json

    branch = payload.get("ref")

    logging.info(branch)

    if branch != f"refs/heads/{DEFAULT_BRANCH}":

        logging.info("Ignored")

        return jsonify({
            "message":"Ignored"
        })

    logging.info("Triggering deployment")

    run()

    return jsonify({
        "message":"Deployment Started"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    leo
