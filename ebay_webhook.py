import hashlib
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_TOKEN = os.environ.get(
    "EBAY_VERIFICATION_TOKEN",
    "CHANGE_THIS_LATER"
)

ENDPOINT_URL = os.environ.get(
    "EBAY_ENDPOINT_URL",
    "CHANGE_THIS_LATER"
)


@app.get("/ebay/marketplace-deletion")
def ebay_challenge():
    challenge_code = request.args.get("challenge_code")

    if not challenge_code:
        return jsonify({"error": "Missing challenge_code"}), 400

    response = (
        challenge_code
        + VERIFICATION_TOKEN
        + ENDPOINT_URL
    )

    challenge_response = hashlib.sha256(
        response.encode("utf-8")
    ).hexdigest()

    return jsonify({
        "challengeResponse": challenge_response
    })


@app.post("/ebay/marketplace-deletion")
def ebay_deletion_notification():
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)