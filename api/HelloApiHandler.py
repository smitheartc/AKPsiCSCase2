from flask_restful import Api, Resource, reqparse
import requests

class HelloApiHandler(Resource):
  def get(self, artist, song):
    artist.replace("%20"," ")
    song.replace("%20"," ")
    resp = requests.get("https://api.lyrics.ovh/v1/{artist}/{song}".format(artist=artist, song=song))
    return resp.json()
    # return {
    #   'resultStatus': 'SUCCESS',
    #   'message': artist,
    #   'song': song
    #   }

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str)
    parser.add_argument('content', type=str)
    args = parser.parse_args()

    print(args)
    # note, the post req from frontend needs to match the strings here (e.g. 'type and 'content')

    request_type = args['type']
    request_json = args['content']
    # ret_status, ret_msg = ReturnData(request_type, request_json)
    # currently just returning the req straight
    ret_status = request_type
    ret_msg = request_json
    print(type(args["content"]))

    if request_type == "lyrics":
      message = args["content"]["artist"]
    else:
      message = "No Msg"
    
    final_ret = {"status": "Success", "message": message}

    return final_ret