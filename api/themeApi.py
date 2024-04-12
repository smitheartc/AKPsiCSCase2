from flask_restful import Api, Resource, reqparse
from sklearn.feature_extraction.text import CountVectorizer
import requests
import json


class themeApi(Resource):

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('lyrics', type=str)
    args = parser.parse_args()

    # note, the post req from frontend needs to match the string here
    lyrics = args['lyrics']

    # changing it to a string format
    lyrics = json.dumps(lyrics)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(lyrics)
    z = vectorizer.vocabulary
        
    #Cleaning up the junk in the first line
    # raw = resp.json()
    # lyrics = raw["lyrics"]
    # index = lyrics.find('\n')  #finding the first \n
    # lyrics = lyrics[index+1:]  #deleting everything before that

    # #Making the return a json
    # lyricList = {"lyrics" : lyrics}
    # response = json.dumps(lyricList)

    return z