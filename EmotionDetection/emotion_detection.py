import requests
import json

def emotion_detector(text_to_analyse):
    # 1. Define the API URL and Headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # 2. Create the JSON payload
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # 3. Make the POST request
    response = requests.post(url, json=myobj, headers=headers)
    
    # 4. Handle errors and empty inputs (Crucial for passing)
    if response.status_code == 400 or not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    # 5. Parse successful response
    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    
    # 6. Extract individual scores
    anger = emotion_predictions['anger']
    disgust = emotion_predictions['disgust']
    fear = emotion_predictions['fear']
    joy = emotion_predictions['joy']
    sadness = emotion_predictions['sadness']
    
    # 7. Find the dominant emotion
    emotions_dict = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    
    # 8. Return the final formatted dictionary
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }


if __name__ == "__main__":
    emotion_response = emotion_detector("That is amazing!")
    with open("2b_application_creation.txt", "w", encoding="utf-8") as file:
        file.write(str(emotion_response))