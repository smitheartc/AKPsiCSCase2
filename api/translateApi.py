from flask_restful import Api, Resource, reqparse
from flask import jsonify
from google.cloud import translate
import os

class translateApi(Resource):


  
  credential_path = r"C:\Users\acrob\AppData\Roaming\gcloud\application_default_credentials.json"
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('language', type=str)
    parser.add_argument('text', type=str)
    args = parser.parse_args()

    PROJECT_ID = "casestudy-419503"
    assert PROJECT_ID
    PARENT = f"projects/{PROJECT_ID}"


    # note, the post req from frontend needs to match the strings here (e.g. 'artist and 'song')
    language = args['language']
    text = args['text']

    client = translate.TranslationServiceClient()

    response = client.translate_text(contents=[text], parent = PARENT, target_language_code=language)
    translatedText = response.translations[0].translated_text
    
    translatedText.replace("&#39",r"\n")


    returnDict = { "text" : translatedText}
    return jsonify(returnDict)
