from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

IAM_APIKEY='YE9iRhlIgTewoZmWNTvQBqtKNEd6VxWm1hN1EGVXIG3w'
authenticator = IAMAuthenticator(IAM_APIKEY)

speech_to_text = SpeechToTextV1(authenticator=authenticator)

def transcribe_from_speech(file_name_path):

    texto_STT = 'No-content'

    with open( file_name_path , 'rb') as audio_file:
        transcripcion = speech_to_text.recognize(audio_file, model='es-MX_BroadbandModel', content_type='audio/ogg')

        ###print("La transcipción de Watson fue:", transcripcion)  ##Es el resultado que trae Watson. Es de tipo DetailedResponse
        response = transcripcion.result #Obtenemos el diccionario de la respuesta de Watson

        enunciados = response['results']
        texto_STT = ""
        for frase in enunciados:
            texto_STT += " "+frase['alternatives'][0]['transcript']
        
    return texto_STT