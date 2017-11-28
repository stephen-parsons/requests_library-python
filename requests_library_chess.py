# Stephen Parsons
# Assignment The Requests Library
# 11/28/17

import requests

def getChessRatings(username):
	r = requests.get("https://api.chess.com/pub/player/"+username+"/stats")
	print "Current Chess.com Ratings for "+username+":"
	print "Rapid Rating: ", r.json()["chess_rapid"]["last"]["rating"]
	print "Blitz Rating: ", r.json()["chess_blitz"]["last"]["rating"]
	print "Bullet Rating: ", r.json()["chess_bullet"]["last"]["rating"]
	print "Daily Rating: ", r.json()["chess_daily"]["last"]["rating"]
