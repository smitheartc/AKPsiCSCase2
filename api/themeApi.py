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

        vectorizer = CountVectorizer(stop_words='english', ngram_range=(1, 2))

        X = vectorizer.fit_transform([lyrics])

        word_counts = X.sum(axis=0)  # Sum the occurrences of each word
        words_freq = [(word, word_counts[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
        
        # Sort the vocabulary based on word counts
        #sortedVocab = sorted(vocabulary.items(), key=lambda item: word_counts[item[1]], reverse=True)

        #Filter out words shorter than 5 letters
        #sortedVocab = [(word, count) for word, count in sortedVocab if len(word) >= 5]

        #print(sortedVocab)
        returnDict = words_freq[:2]

        return jsonify(returnDict)