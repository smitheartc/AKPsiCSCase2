from flask_restful import Api, Resource, reqparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
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
        lyrics = lyrics.replace(r"\n", " ")

        #change stop words (what words are important vs not)
        sw = set(ENGLISH_STOP_WORDS)
        sw.update(['ha', 'oh', 'll', 'yeah'])
        list_sw = list(sw)

        #initialize countvectorizer, 
        vectorizer = CountVectorizer(stop_words=list_sw, ngram_range=(1, 2))
        
        #giving the CV the lyrics
        X = vectorizer.fit_transform([lyrics])

        # Sum the occurrences of each word
        word_counts = X.sum(axis=0)  

        x = None
        mc = -1
        # iterate over all the words in the vocab items and get most frequently occuring word
        for word, idx in vectorizer.vocabulary_.items():
            curr = word_counts[0, idx]
            if curr > mc:
                x = word
                mc = curr
        
        #Making the return a json
        them = {"theme" : x}
        return jsonify(them)