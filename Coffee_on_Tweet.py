##for this project i used tweepy Liberay 
##Import Libraries that will be used to make the code run

import tweepy
from tweepy import OAuthHandler
import serial
import time

##authenticate yourself with twitter project

ckey = 'ifcRt3ExUgK6UlB8vkTIFbd74'
csecret = 'TjfnvR5XMcBKiGW0hNKU2izldnCeznpJ690QNoo2kxeFCDre6k'
atoken = '852906193202708480-WsYGolWZcPARMpVZtdHjjskv9CtwDOb'
asecret = 'ULa7RFoOVcMZ2chJFWaw1e7Z6ZUZJmRchcUrfJ3YX7n6E'


auth = OAuthHandler(ckey, csecret) 
auth.set_access_token(atoken, asecret)
auth.secure = True
api = tweepy.API(auth)

##set to your serial port for the adurino 
ser = serial.Serial('/dev/cu.wchusbserial1410', 921600)

## check serial port
def checkokay():
	ser.flushInput()
	time.sleep(3)
	line=ser.readline()
	time.sleep(3)

	if line == ' ':
		line=ser.readline()
	print 'here'
## Welcome message
print 'Welcome To Coffee On Tweet'

#create switch on funcrion 
def switchon():
	status = [] 
	x = 0
	
	status = api.user_timeline('Coffee Boy') ##grab latest statuses from the user
	
	checkIt = [s.text for s in status] ##put status in an array

	drip = checkIt[0].split() ## this will split first tweet into words

	## check for match and write to serial if match
	if drip[0] == '#switchon':
		print 'Tweet Recieved, Switching On Coffee Maker'
		ser.write('1')
	elif drip[0] == '#switchoff': ##break if done
		ser.write('0')
		print 'Switched Off Coffee Maker, Awaiting for more instructions instructions.'
	else:
		ser.write('0')
		print 'Awaiting Tweet instruction'
		
while 1:
	switchon() ## call switchon function
	time.sleep(10) ## sleep for 10 seconds to avoid rate limiting
	
