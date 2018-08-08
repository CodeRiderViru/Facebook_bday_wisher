# this code is for send birthday wishes automatically on facebook

from facepy import GraphAPI
import time
import random
#token u have to generate for your own profile.  
token='Your User access token here for your facebook profile'

graph=GraphAPI(token)

friend_list = graph.get("me/friends?fields=birthday,name")

birthday_wishes=["Happy birthday yr,may god bless u :) ",
"Wish u very Happy Birthday ,party hard ,keep smiling :) ",
"Happy Birthday Bhai ,stay blessed :) ",
"Happy Birthday to you :) "]


localtime=time.localtime(time.time())
month_day=[localtime[1],localtime[2]]

for friend in friend_list['data']:
	
	if friend.has_key('birthday'):
		bday=friend['birthday'].split('/')
		if int(bday[0]) == month_day[0]  and int(bday[1]) == month_day[1]:
			print(friend['name'])
			bday_wish=birthday_wishes[random.randint(0,3)]
			graph.post(friend['id']+ '/feed' ,0,message=bday_wish)
			print "wished" +friend['name']
			

