import requests


artist = input("Enter the artist: ")
song = input("Enter the song: ")

r = requests.get("https://api.lyrics.ovh/v1/{artist}/{song}".format(artist=artist, song=song))

lyrics = r.json().get("lyrics")
