"""
This module deploys the Emotion Detection application as a web application using Flask.
It provides endpoints to render the main page and to process text input for emotion detection.
"""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the main index.html page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():  # pylint: disable=invalid-name
    """
    Handle GET requests to perform emotion detection.

    Expects a query parameter 'textToAnalyze' containing the input text.
    Returns a JSON response with the emotion scores and the dominant emotion
    formatted as:

    For the given statement, the system response is 'anger': <anger>, 'disgust': <disgust>,
    'fear': <fear>, 'joy': <joy> and 'sadness': <sadness>. The dominant emotion is
    <dominant_emotion>.

    If the input is invalid (empty text), an error message is returned.
    """
    text = request.args.get("textToAnalyze")
    if not text or not text.strip():
        return jsonify({"error": "Invalid input. Please provide some text."}), 400

    result = emotion_detector(text)

    # Construct the response string in the requested format.
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_str})


if __name__ == "__main__":
    # Run the Flask development server on all interfaces on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
