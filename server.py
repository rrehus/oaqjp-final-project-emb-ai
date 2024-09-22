"""Web Deployment of Emotion Detector App with Error Handling"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """Display response from Emotion Detector"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"

    # Return a formatted string with the sentiment label and score
    return f"<div>For the given statement, the system response is 'anger': {response['anger']}, \
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': \
    {response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}</b></div>"

@app.route("/")
def render_index_page():
    """Index page rendering"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
