from flask_restful import Resource, reqparse
from flask import jsonify
import azapi
import requests

class lyricApi(Resource):

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('artist', type=str)
    parser.add_argument('song', type=str)
    args = parser.parse_args()

    #note, the post req from frontend needs to match the strings here (e.g. 'artist and 'song')
    artist = args['artist']
    song = args['song']

    
    API = azapi.AZlyrics('google', accuracy=0.5)

    API.artist = artist
    API.title = song

    try:
      API.getLyrics(save=False)
      lyrics = API.lyrics
    except:
      lyrics = ""
    # print("\nHere are the lyrics: ||" + API.lyrics + "||\n")
    
    #first api failed, trying second api
    if (lyrics == ""):
      print("kicking into second gear!!!\n\n")
      resp = requests.get("https://api.lyrics.ovh/v1/{artist}/{song}".format(artist=artist, song=song))
      
      # Cleaning up the junk in the first line
      raw = resp.json()
      lyrics = raw["lyrics"]
      print(lyrics)
      index = lyrics.find('\n')  #finding the first \n
      lyrics = lyrics[index+1:]  #deleting everything before that

    #Making the return a json
    lyricList = {"lyrics" : lyrics}
 
    return jsonify(lyricList)