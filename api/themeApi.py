from flask_restful import Api, Resource, reqparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.decomposition import LatentDirichletAllocation
from flask import jsonify
import json
import numpy as np

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
        sw.update(['ha', 'oh', 'll', 'yeah', 'like', 'uh', 'nah', 'la', 'yo', 've', 'got'])
        list_sw = list(sw)

        #initialize countvectorizer, removing stop words and looking for 1-2 word length phrases
        vectorizer = CountVectorizer(stop_words=list_sw, ngram_range=(1, 2), max_features=1000)
        
        #giving the CV the lyrics
        cv = vectorizer.fit_transform([lyrics])

        #using LDA to get a word that most represents the topic
        lda = LatentDirichletAllocation(n_components=5, random_state=0)  # One topic

        #fitting it to the document term matrix
        lda.fit(cv)

        #calculate the importances of each topic
        importances = np.sum(lda.components_, axis=1) 
        
        #find most important topic
        highest = lda.components_[np.argmax(importances)]

        #get all the stored words
        names = vectorizer.get_feature_names_out()

        # Get indices of the top 2 words/phrases
        top_indices = highest.argsort()[-2:] 
        top_words = [names[i] for i in reversed(top_indices)]
        message = " ".join(top_words)

        # makes sure that message is 2 words at the max
        if len(message.split()) > 2:
            message = " ".join(message.split()[:2])
        
        #Making the return a json
        theme = {"theme" : message}
        return jsonify(theme)