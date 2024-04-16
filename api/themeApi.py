from flask_restful import Api, Resource, reqparse
from sklearn.feature_extraction.text import CountVectorizer
from flask import jsonify
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

        #initialize countvectorizer, configuring it to consider key words
        vectorizer = CountVectorizer(stop_words='english', ngram_range=(1, 2))
        
        #giving the CV the lyrics
        X = vectorizer.fit_transform([lyrics])

        # Sum the occurrences of each word
        word_counts = X.sum(axis=0)  
        words_freq = [(word, word_counts[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)

        #getting the top 2 words freq words
        returnDict = words_freq[:2]
        
        #Making the return a json
        return jsonify(returnDict)