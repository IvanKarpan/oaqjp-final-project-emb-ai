"""
This module provides the emotion_detector function which uses the Watson NLP
EmotionPredict API to analyze text and return emotion scores along with the
dominant emotion.
"""

import json

import requests


def emotion_detector(text_to_analyse):
    """
    Sends a POST request to the Watson NLP EmotionPredict endpoint with the given text.
    Processes the nested JSON response to extract emotion scores and determine the
    dominant emotion.

    The expected response format is:
    {
        'emotionPredictions': [{
            'emotion': {
                'anger': <value>,
                'disgust': <value>,
                'fear': <value>,
                'joy': <value>,
                'sadness': <value>
            },
            ... other keys ...
        }],
        ... other keys ...
    }

    Args:
        text_to_analyse (str): The text to analyze for emotion.

    Returns:
        dict: A dictionary containing the emotion scores for 'anger', 'disgust', 'fear',
              'joy', 'sadness' and the 'dominant_emotion' which is the emotion with the highest score.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1"
        "/watson.runtime.nlp.v1"
        "/NlpService"
        "/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=payload, timeout=10)
    response_json = json.loads(response.text)

    # Extract the nested emotion scores from the first prediction in 'emotionPredictions'
    emotion_data = response_json.get("emotionPredictions", [{}])[0].get("emotion", {})

    anger = emotion_data.get("anger", 0)
    disgust = emotion_data.get("disgust", 0)
    fear = emotion_data.get("fear", 0)
    joy = emotion_data.get("joy", 0)
    sadness = emotion_data.get("sadness", 0)

    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }

    # Determine the dominant emotion by selecting the key with the highest score.
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions


# Test the function if this file is run as a script.
if __name__ == "__main__":
    # Test input as specified in the instructions.
    TEST_TEXT = "I am so happy I am doing this."
    result = emotion_detector(TEST_TEXT)
    print("Formatted emotion detection output:", result)
