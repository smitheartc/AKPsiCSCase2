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

        Y = vectorizer.vocabulary_

        sortedVocab = sorted(vectorizer.vocabulary_.items(), key=lambda item: item[1], reverse=True)


        # feature_names = vectorizer.get_feature_names_out()

        # df = pd.DataFrame(X.toarray(), columns=feature_names)

        # sentiment_scores = np.zeros(df.shape[1])
        # for i in range(df.shape[1]):
        #     word = feature_names[i]
        #     if word in positive_words:
        #         sentiment_scores[i] += 1
        #     elif word in negative_words:
        #         sentiment_scores[i] -= 1

        # # Get the top 2 words with the highest sentiment scores
        # top_2_words = np.argsort(sentiment_scores)[-2:]

        #Making the return a json
        jsonRet = {"theme" : sortedVocab[:2]}
        response = json.dumps(jsonRet)

        return response