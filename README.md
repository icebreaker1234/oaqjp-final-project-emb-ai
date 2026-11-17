# Final project

This repository contains a Flask emotion detection application built with IBM Watson NLP. It analyzes text for anger, disgust, fear, joy, and sadness, returns the score for each emotion, and identifies the dominant emotion.

## Project files

- `EmotionDetection/emotion_detection.py` calls Watson NLP and formats the emotion results.
- `EmotionDetection/__init__.py` exposes `emotion_detector` from the package.
- `server.py` serves the web interface and handles blank input.
- `test_emotion_detection.py` contains unit tests for all five dominant emotions.
- `templates/index.html` and `static/` provide the web interface.

## Run the application

Install dependencies with `python3 -m pip install -r requirements.txt`, then start the server with `python3 server.py`. Open `http://127.0.0.1:5001` in a browser.

The Watson NLP service endpoint can be changed with the `WATSON_EMOTION_URL` environment variable.
