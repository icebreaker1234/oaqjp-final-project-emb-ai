"""Flask web server for the Watson emotion detection application."""

import os

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.get("/")
def home():
    """Render the emotion detector form."""
    return render_template("index.html")


@app.get("/emotionDetector")
def detect_emotion():
    """Return emotion scores for the text entered in the web form."""
    text_to_analyse = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyse)
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5001")), debug=False)
