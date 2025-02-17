import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json=myobj, headers=header)  

    # Return the response text from the API
    #return response.text  

    # Convert response to a dictionary
    formatted_response = json.loads(response.text)

    # Extract emotions from the first prediction
    predictions = formatted_response.get("emotionPredictions", [{}])
    emotions = predictions[0].get("emotion", {})

    # Extract individual emotion scores
    anger = emotions.get('anger', 0.0)
    disgust = emotions.get('disgust', 0.0)
    fear = emotions.get('fear', 0.0)
    joy = emotions.get('joy', 0.0)
    sadness = emotions.get('sadness', 0.0)

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

# Example usage for fast testing
#text = "I am so happy I am doing this"
#print(emotion_detector(text))
