"""Emotion detection using IBM Watson NLP's hosted service."""

import os

import requests

WATSON_EMOTION_URL = os.getenv(
    "WATSON_EMOTION_URL",
    "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"


def emotion_detector(text_to_analyse):
    """Return five emotion scores and the dominant emotion for input text.

    Empty text or an HTTP 400 response returns None values, allowing the web
    application to show its invalid-input message instead of crashing.
    """
    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(WATSON_EMOTION_URL, json=payload, headers=headers, timeout=30)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response.raise_for_status()
    prediction = response.json()["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(prediction, key=prediction.get)
    return {
        "anger": prediction["anger"],
        "disgust": prediction["disgust"],
        "fear": prediction["fear"],
        "joy": prediction["joy"],
        "sadness": prediction["sadness"],
        "dominant_emotion": dominant_emotion,
    }
