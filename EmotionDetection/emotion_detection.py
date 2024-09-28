import requests,json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsoninput =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url,json = jsoninput,headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dom_emotion_val = max(emotions.values())

        for e in emotions:
            if emotions[e] == dom_emotion_val:
                emotions['dominant_emotion'] = e
                break
    elif response.status_code == 400:
        emotions = {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
            }

    return emotions