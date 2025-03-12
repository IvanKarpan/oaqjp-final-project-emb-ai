"""
Unit tests for the emotion_detector function in the EmotionDetection package.
This module verifies that the dominant emotion returned for various input texts
matches the expected outcome.
"""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Unit test cases for the emotion_detector function."""

    def test_joy(self):
        """Test that the dominant emotion is 'joy' for a positive statement."""
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertEqual(
            result.get("dominant_emotion"),
            "joy",
            f"Expected 'joy' for input: {text}, got: {result.get('dominant_emotion')}",
        )

    def test_anger(self):
        """Test that the dominant emotion is 'anger' for an angry statement."""
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertEqual(
            result.get("dominant_emotion"),
            "anger",
            f"Expected 'anger' for input: {text}, got: {result.get('dominant_emotion')}",
        )

    def test_disgust(self):
        """Test that the dominant emotion is 'disgust' for a statement expressing disgust."""
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(
            result.get("dominant_emotion"),
            "disgust",
            f"Expected 'disgust' for input: {text}, got: {result.get('dominant_emotion')}",
        )

    def test_sadness(self):
        """Test that the dominant emotion is 'sadness' for a statement expressing sadness."""
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(
            result.get("dominant_emotion"),
            "sadness",
            f"Expected 'sadness' for input: {text}, got: {result.get('dominant_emotion')}",
        )

    def test_fear(self):
        """Test that the dominant emotion is 'fear' for a statement expressing fear."""
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(
            result.get("dominant_emotion"),
            "fear",
            f"Expected 'fear' for input: {text}, got: {result.get('dominant_emotion')}",
        )


if __name__ == "__main__":
    unittest.main()
