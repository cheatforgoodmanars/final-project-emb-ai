"""
Flask server for Emotion Detection API.

This script sets up a Flask web application that:
- Accepts text input from users via an HTML interface
- Calls the `emotion_detector` function to analyze emotions in the text
- Returns the detected emotions as a response
"""
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("NLP - Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function.
    '''
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again."

    #return response
    return (
        f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
