import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json=myobj, headers=header)  

    # Convert response to a dictionary
    formatted_response = json.loads(response.text)

    # Handle error responses
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        print("Invalid input ! Try again.")

    elif response.status_code != 200: # for other error types
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        print("Invalid input ! Try again.", response.status_code)

    # Extract emotions from the first prediction
    predictions = formatted_response.get("emotionPredictions", [{}])
    emotions = predictions[0].get("emotion", {})

    # Initialize default values (to avoid undefined variables)
    anger = emotions.get('anger')
    disgust = emotions.get('disgust')
    fear = emotions.get('fear')
    joy = emotions.get('joy')
    sadness = emotions.get('sadness')

    # Determine dominant emotion
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the formatted dictionary
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    } 