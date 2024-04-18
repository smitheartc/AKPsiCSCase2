from flask_restful import Api, Resource, reqparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.decomposition import LatentDirichletAllocation
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
        sw.update(['ha', 'oh', 'll', 'yeah', 'like', 'uh', 'nah'])
        list_sw = list(sw)

        #initialize countvectorizer, removing stop words and looking for 1-2 word length phrases
        vectorizer = CountVectorizer(stop_words=list_sw, ngram_range=(1, 2))
        
        #giving the CV the lyrics
        cv = vectorizer.fit_transform([lyrics])

        #using LDA to get a word that most represents the topic
        lda = LatentDirichletAllocation(n_components=1, random_state=0)  # One topic

        #fitting it to the document term matrix
        lda.fit(cv)

        #getting the names within the document term matrix
        names = vectorizer.get_feature_names_out()

        #iterates throught the lda
        for topic_idx, topic in enumerate(lda.components_):
            message = " ".join([names[i] for i in topic.argsort()[:-2:-1]])
        
        #Making the return a json
        theme = {"theme" : message}
        return jsonify(theme)