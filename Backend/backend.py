import requests



from flask import Flask
from flask import url_for #this implements a way to make url building easier, but need to still figure it out
from flask import request, jsonify #not used yet, may use
import requests

app = Flask(__name__)

#over here, create a sort of temporary storage, like a cache, that will store
#the lyrics so that it can be translated

@app.route("/<artist>/<song>") #by default, uses GET
def lyrics(artist, song):
    resp = requests.get('https://api.lyrics.ovh/v1/<artist>/<song>')
    return resp.json()

#function above currently is facing issues because it does not treat
# the %20 symbol as a space. I was trying to see if I could use
#urllib to fix this but was not able to figure it out yet.
     
#now, using a POST, need to create a function that takes the lyrics from the cache and translates it
#and then finally, using a GET, create a function that takes the lyrics and returns the genre

if __name__ == '__main__':
    app.run(debug=True)

#artist = input("Enter the artist: ")
#song = input("Enter the song: ")

#r = requests.get("https://api.lyrics.ovh/v1/{artist}/{song}".format(artist=artist, song=song))

#lyrics = r.json().get("lyrics")
