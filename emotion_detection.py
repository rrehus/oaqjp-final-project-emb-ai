import requests
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  
    response = json.loads(response.text)
    emotions = response["emotionPredictions"][0]["emotion"]
    max_emotion_score = max(emotions.values())
    emotions["dominant_emotion"] = [key for key,value in emotions.items() if value==max_emotion_score][0]
    return emotions

