import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
import json

song = input("entrez chanson plz : ")
data = dict()
newSong = ""
for i in song:
	if i == " ":
		newSong+="+"
	else:
		newSong+=i
		
song=newSong

url = "https://www.youtube.com/results?search_query="+song+"+lyrics"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
nameString =  str(soup)

bksl = "\\"
stri = "\""

url = re.findall("\w[\w(a-z)]+\="+bksl+stri+"+\/+\w[a-z]+\?+\w+\=+\w+"+bksl+stri, nameString)[0]
stripUrl = url[7:-1]

youtubeURL = "http://youtube.com/"+stripUrl

#print(youtubeURL)
data["url"]=youtubeURL


page = urllib2.urlopen(youtubeURL)
soup = BeautifulSoup(page, "html.parser")
nameString = str(soup)


liste1 = re.findall("\w[A-z0-9 ="+stri + "-]+\>+\d+:+\d+", nameString)
length = liste1[0]

if len(length) > 28:
	length = length[-5:(len(length))]
else:
	length = length[-4:(len(length))]


#print(length)
data["length"]=length
lengthInSec = 0
if len(length) == 4:
	lengthInSec = (int(length[0])*60)+(int(length[2])*10)+int(length[3])
elif len(length) == 5:
	lengthInSec = (((int(length[0])*10)+int(length[1]))*60)+(int(lengtt[3])*10)+int(length[4])

data["lengthInSec"]=lengthInSec
print(json.dumps(data, indent=4))







