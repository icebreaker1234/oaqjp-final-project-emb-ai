"""Unit tests for the emotion detector response formatting."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check dominant-emotion selection and output keys."""

    def _response(self, dominant):
        scores = {"anger": 0.1, "disgust": 0.1, "fear": 0.1, "joy": 0.1, "sadness": 0.1}
        scores[dominant] = 0.6
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"emotionPredictions": [{"emotion": scores}]}
        response.raise_for_status.return_value = None
        return response, scores

    def _check_dominant_emotion(self, text, expected):
        response, scores = self._response(expected)
        with patch("EmotionDetection.emotion_detection.requests.post", return_value=response):
            result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], expected)
        self.assertEqual(set(result), {"anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"})
        self.assertEqual(result[expected], scores[expected])

    def test_joy(self):
        self._check_dominant_emotion("I am glad this happened", "joy")

    def test_anger(self):
        self._check_dominant_emotion("I am really mad about this", "anger")

    def test_disgust(self):
        self._check_dominant_emotion("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        self._check_dominant_emotion("I am so sad about this", "sadness")

    def test_fear(self):
        self._check_dominant_emotion("I am really afraid that this will happen", "fear")

    def test_blank_input_returns_empty_scores(self):
        result = emotion_detector("   ")
        self.assertEqual(result["dominant_emotion"], None)
        self.assertTrue(all(result[key] is None for key in ("anger", "disgust", "fear", "joy", "sadness")))


if __name__ == "__main__":
    unittest.main()
