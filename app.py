from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
#from flask_cors import CORS #comment this on deployment
from api.lyricApi import lyricApi
from api.translateApi import translateApi
from api.themeApi import themeApi

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
#CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(lyricApi, '/lyrics/')
api.add_resource(translateApi, '/translate/')
api.add_resource(themeApi, '/theme/')