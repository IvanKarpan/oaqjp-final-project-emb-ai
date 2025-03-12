"""
This module provides an emotion_detector function that uses Watson NLP
to detect emotions from text.
"""

import requests


def emotion_detector(text_to_analyse):
    """
    Sends a POST request to the Watson NLP EmotionPredict endpoint with the given text.

    Args:
        text_to_analyse (str): The text to analyze for emotion.

    Returns:
        str: The text attribute from the response containing the emotion detection result.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    response = response = requests.post(url, headers=headers, json=payload, timeout=10)
    return response.text


# Test the function if this file is run as a script
if __name__ == "__main__":
    TEST_TEXT = "I love this new technology."
    print("Emotion detection output:", emotion_detector(TEST_TEXT))
