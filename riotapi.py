import json
import urllib2

def get_summoner_id(summoner):
	url_summoner = summoner.replace(' ', '%20')
	data_summoner = summoner.replace(' ', '')
	url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"+url_summoner+"?api_key=da5ff0e5-d859-4d7b-a3a1-c8df657df6c9"
	json_obj = 	urllib2.urlopen(url)
	data = json.load(json_obj)
	summoner_id = data[data_summoner]['id']

	return summoner_id

def season_info(season,summoner_id):
	if season == 'season3':
		season = 'SEASON3'
	elif season == 'season4':
		season = 'SEASON2014'
	elif season == 'season5':
		season == 'SEASON2015'

	url = "https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/"+str(summoner_id)+"/ranked?season="+season+"&api_key=da5ff0e5-d859-4d7b-a3a1-c8df657df6c9"
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)

	for item in data['champions']:
		print item['stats']['totalQuadraKills']


summoner = raw_input("Enter summoner name: ")
summoner_id = get_summoner_id(summoner)
season = raw_input("Enter \"season3\",\"season4\", or \"season5\" to choose a season to display info about: ")
season_info(season,summoner_id)