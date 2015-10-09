import json
import urllib2
from lists import keylist
from lists import namelist
from lists import menu
import plotly.plotly as py
from plotly.graph_objs import *

key = '9c810c33-25b4-4857-b974-5576d0eefc38'
dataValues = []
champNames = []
total_count = 1

def graph_info():
	data = Data([
	    Bar(
	        x= champNames,
	        y= dataValues
	   )
	])
	plot_url = py.plot(data, filename='basic-bar')

#Get summoner ID by name
def get_summoner_id(summoner,region):
	url_summoner = summoner.replace(' ', '%20')
	data_summoner = summoner.replace(' ', '')
	url = "https://"+str(region)+".api.pvp.net/api/lol/"+str(region)+"/v1.4/summoner/by-name/"+url_summoner+"?api_key=" + key
	json_obj = 	urllib2.urlopen(url)
	data = json.load(json_obj)
	summoner_id = data[data_summoner]['id']

	return summoner_id


def season_info_single(season,summoner_id,doThis,champOrAll,region):
	if season == 'season3':
		season = 'SEASON3'
	elif season == 'season4':
		season = 'SEASON2014'
	url = "https://"+str(region)+".api.pvp.net/api/lol/"+str(region)+"/v1.3/stats/by-summoner/"+str(summoner_id)+"/ranked?season="+season+"&api_key=" + key
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	found = False
	champion = champOrAll.replace(' ','')

	for item in data['champions']:
		if str(id_to_name(item['id'])).lower() == champion.lower():
			print str(namelist[doThis]) + " by " + str(id_to_name(item['id'])) + ": " + str(item['stats'][keylist[doThis]]) 
			found = True
			break
	if found == False:
		print("You did not use " + champion.title() + " on " + season)

#Display Information about a certain ranked season for all champions
def season_info(season,summoner_id, doThis,region):
	if season == 'season3':
		season = 'SEASON3'
	elif season == 'season4':
		season = 'SEASON2014'
	url = "https://"+str(region)+".api.pvp.net/api/lol/"+str(region)+"/v1.3/stats/by-summoner/"+str(summoner_id)+"/ranked?season="+season+"&api_key=" + key
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	total = 0
	count = 0


	for item in data['champions']:
			champ_name = str(id_to_name(item['id']))
			champNames.append(champ_name)
			if str(champ_name) == '0':
				champ_name = 'All'

			if champ_name != 'All':	
				thisData = str(item['stats'][keylist[doThis]]) 
				dataValues.append(thisData)
				print str(count) + ". " + str(namelist[doThis]) + " by " + champ_name + ": " + str(item['stats'][keylist[doThis]]) 
				count += 1
			if champ_name == 'All':
				total = item['stats'][keylist[doThis]]
	print str(namelist[doThis]) + " by All: " + str(total)
	total_count = count
		


#Change champion ID  to name
def id_to_name(champ_id):
	if champ_id != 0:
		url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(champ_id)+"?locale=en_US&api_key=" + key
		json_obj = urllib2.urlopen(url)
		data = json.load(json_obj)
		champ_name = data['key']

		return champ_name

	else:
		return 0



running = True
graph = False
print('Type in \'q\' or \'Q\' to exit the program.\n\n')
summoner = raw_input("Enter summoner name: ")

if summoner.lower() == 'q':
	quit()


region = raw_input('Enter region (na, eu, kr, br eune, euw, lan, las, oce, ru, tr): ')

if region.lower() == 'q':
	quit()

while running == True:
	season = raw_input("Enter \"season3\" or \"season4\" to choose a season to display info about: ")
	if season.lower() == 'q':
		running = False
		break
	"""
	graphDecision = raw_input("Create Graph? (yes or no) : ")
	if graphDecision.lower() == 'yes':
		graph = True"""

	champOrAll = raw_input('Enter the name of a Champion to find his stats or \'all\' to display stats of all champions: ')
	if champOrAll.lower() == 'q':
		runnig = False
		break

	print(menu)

	doThis = raw_input("Choose One: ")
	if doThis.lower() == 'q':
		running = False
		break


	summoner_id = get_summoner_id(summoner.lower(),region)

	if champOrAll.lower() == 'all':
		season_info(season,summoner_id, doThis, region)
	elif champOrAll != 'all':
		season_info_single(season,summoner_id, doThis,champOrAll, region)
	

	graph_info()
	plot_url = None







