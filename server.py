"""
Flask server for Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the text provided in request parameters and returns formatted result string.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyze the emotion
    response = emotion_detector(text_to_analyze)

    # Extract dominant emotion
    dominant_emotion = response.get('dominant_emotion')

    # Error handling for invalid/blank text
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Format the output string for valid response
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the index.html template.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
