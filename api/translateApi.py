from flask_restful import Resource, reqparse
from flask import jsonify
from google.cloud import translate
import os
import re

class translateApi(Resource):

  credential_path = r"application_default_credentials.json"
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('language', type=str)
    parser.add_argument('text', type=str)
    args = parser.parse_args()

    #google api boilerplate
    PROJECT_ID = "casestudy-419503"
    assert PROJECT_ID
    PARENT = f"projects/{PROJECT_ID}"


    #note, the post req from frontend needs to match the strings here (e.g. 'language and 'text')
    language = args['language']
    text = args['text']

    print(text)
    #replacing newlines with | to send to google translate
    text = text.replace('\n', ' | ')
    print(text)
    #actual translation call to Google Translate API 
    client = translate.TranslationServiceClient()
    response = client.translate_text(contents=[text], parent = PARENT, target_language_code=language)
    translatedText = response.translations[0].translated_text

    #removing junk data that got messed up when sending to translate
    translatedText = re.sub('.&#39;', '', translatedText) 

    #replacing | with newlines for the return
    translatedText = translatedText.replace('| ', '\n')


    #formatting the data to return properly
    returnDict = { "text" : translatedText}
    return jsonify(returnDict)
