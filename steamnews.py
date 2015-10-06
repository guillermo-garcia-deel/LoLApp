import json
import urllib2


key = "FDC4EC5F79B298BC866751AFC0AEFA68"

def steam_news_writer(count, appid):
	url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid="+str(appid)+ "&count="+str(count) + "&maxlength=300&format=json"
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	count = 1
	foo = open(str(appid) + 'Info.txt', 'w')

	for item in data['appnews']['newsitems']:
		foo.write(str(count) + " TITLE: " + str(item['title']) + "\nCONTENT: " + str(item['contents']) + "\nURL: " + str(item['url']) + "\n\n\n")
		#foo.write('%d. Title: %r\nCONTENT: %r\nURL: %r\n\n\n') % (count ,str(item['title']),str(item['contents']),str(item['url']))
		count+=1
		
		
	print("File Created.")
	foo.close()



appid = raw_input("Enter AppId: ")
count = raw_input("Enter Number of News: ")
steam_news_writer(count,appid)