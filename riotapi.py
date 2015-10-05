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


	url = "https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/"+str(summoner_id)+"/ranked?season="+season+"&api_key=da5ff0e5-d859-4d7b-a3a1-c8df657df6c9"
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	
	print data
	#for name,value in data['champions'].items():
		#for name,value in value['stats'].items():
			#print "Total Minion Kills with champion Name = " + str(id_to_name(item['id'])) + ": " + str(item['stats']['totalMinionKills'])
		#print item['stats']['totalQuadraKills']

def id_to_name(champ_id):
	url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(champ_id)+"?api_key=da5ff0e5-d859-4d7b-a3a1-c8df657df6c9"
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	champ_name = str(data['name'])

	return champ_name



summoner = raw_input("Enter summoner name: ")
summoner_id = get_summoner_id(summoner)
season = raw_input("Enter \"season3\" or \"season4\" to choose a season to display info about: ")
season_info(season,summoner_id)