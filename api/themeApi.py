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

        vectorizer = CountVectorizer()

        X = vectorizer.fit_transform([lyrics])

        word_counts = X.toarray().sum(axis=0)  # Sum the occurrences of each word
        vocabulary = vectorizer.vocabulary_
        
        # Sort the vocabulary based on word counts
        sortedVocab = sorted(vocabulary.items(), key=lambda item: word_counts[item[1]], reverse=True)

        #Filter out words shorter than 5 letters
        sortedVocab = [(word, count) for word, count in sortedVocab if len(word) >= 5]

        sum_words = X.sum(axis=0)
        words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)

        print(sortedVocab)

        #Making the return a json
        jsonRet = {"theme" : sortedVocab[:2]}

        returnDict = { "theme word 1" : jsonRet["theme"][0][0], "theme word 2" : jsonRet["theme"][1][0]}

        return jsonify(returnDict)