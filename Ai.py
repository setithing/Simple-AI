import json
import random
import time
import datetime
import string

def saveData(inArray, outArray, user):
	print "saving"
		
		
	store1 = '"inData":['
	for i, item in enumerate(inArray):
		if(i == (len(inArray)-1)):
			store1 = store1 + '{"id":"' + str(inArray[i]) + '"}'
		else:
			store1 = store1 + '{"id":"' + str(inArray[i]) + '"},'
	
	store1 = store1 + ']'
	
	store2 = '"outData":['
	for i, item in enumerate(outArray):
		if(i == (len(inArray)-1)):
			store2 = store2 + '{"id":"' + str(outArray[i]) + '"}'
		else:
			store2 = store2 + '{"id":"' + str(outArray[i]) + '"},'
	
	store2 = store2 + ']'
	
	store3 = '"userName":"' + usersnamel + '"'
	store4 = '"pcLName":"' + lname + '"'
	store5 = '"pcRName":"' + fname + '"'

	store = '{'+ store5+','+store4 +','+ store3 + ',' + store1 + ',' + store2 + '}'

	fileJson = open("data/brain.json", "w")
	fileJson.write(store)
	fileJson.close()


#variable decalring

#computer names
firstnames = ["Mark","Ben","Tom","Tim","George","Lily","Megan","Linus","Abbie","Elizabeth","Ryan","James","John","Robert","Michael","William","David","Richard","Charles","Joseph","Thomas","Christopher","Daniel","Paul","Mark","Donald","George","Kenneth","Steven","Edward","Brian","Ronald","Anthony","Kevin","Jason","Matthew","Gary","Timothy","Jose","Larry","Mary","Patricia","Linda","Barbara","Elizabeth","Jennifer","Maria","Susan","Margaret","Dorothy","Lisa","Nancy","Karen","Betty","Helen","Sandra","Donna","Carol","Ruth","Sharon","Michelle","Laura","Sarah","Kimberly","Deborah","Jessica","Shirley"] #NO MORE NAMES!
lastnames = ["Smith","Johnson","Williams","Jones","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson","Thomas"]



usernamel = ""

message = "Hello "

inMessage = []
outMessage = []
feelings = [["crap","rubbish","not good"],["evil","bad","annoyed"],["ok","well","meh"],["good","simple","cool"],["brilliant","awesome","totally awesome"]]
feeling = 3
boundaries = [["rubbish","idiot","annoying","evil"],["awesome","good","cool"]]
## boundaries go 0*3, 1*3, 2*3, 3*3, etc 1-15 (max boundary = 3*5)

data = ""
dataSplit = []
splitBuffer = []

wordMatch = []
highWord = 0
noHigh = 1
match = 0

done = 0

debug = 1

chats = 0

running = 1

olddata = "Hello"

#loading and processing json file
jsonFile = open('data/brain.json').read()

brain = json.loads(jsonFile)


#retriving data from json
for i, item in enumerate(brain["inData"]):
	inMessage.append(brain["inData"][i]["id"])
	outMessage.append(brain["outData"][i]["id"])
	wordMatch.append(0)
	
usersnamel = brain["userName"]
lname = brain["pcLName"] 
fname = brain["pcRName"]

print len(brain["inData"])

now = time.strftime("%H:%M:%S")

print "waking up..."

now = time.strftime("%H:%M:%S")# uses a string make in time to create the time
if lname == "":
	# picking computers name
	lname = lastnames[random.randint(0,len(lastnames)-1)]
	fname = firstnames[random.randint(0,len(firstnames)-1)]
#combineing names
namel = fname + " " + lname
if usersnamel == "":
	usersnamel = raw_input(now + " " + namel + ": What is your name?\n" + now + " You: ")


age = random.randint(14,60)

print now + " " + namel + ": " + message

while running == 1:
	
	data = raw_input(now + " " + usersnamel + ": ")
	
	#commands
	if data == "*LIST":
		for i, item in enumerate(inMessage):
			print inMessage[i], ", ", outMessage[i]
		done = 2
		
	if data == "*SAVE":
		print "saving"
		
		saveData(inMessage, outMessage, usernamel)
		
		done = 2
	
	if data == "*EXIT":
		nnow = time.strftime("%H:%M:%S")# uses a string make in time to create the time
		print now + " " + namel + ": Bye see you soon"

		
		print "saving"
		
		saveData(inMessage, outMessage, usernamel)
		
		done = 2
		running = 0
		
	if data == "*THINK":
		q = random.randint(0,(len(inMessage)-1))
		now = datetime.datetime.now()
		p = raw_input(now + " " + namel + ": " + inMessage[q] + "\nYou: ")
		inMessage.append(inMessage[q])
		outMessage.append(p)
		wordMatch.append(0)
		done = 2
		
	if data == "*DEBUG":
		if debug == 0:
			debug = 1
		else:
			debug = 0
		done = 2
		
	if data == "*WRONG":
		replace2 = raw_input("Please correct my mistake: ")
		inMessage.append(olddata)
		outMessage.append(replace2)
		wordMatch.append(0)
		done = 2
		
	#end of commands
	
	#string checking
	olddata = data.lower()
	data = data.lower()
	
	for i in range(0,len(boundaries[0])-1):
		pos = data.find(boundaries[0][i])
		if pos < 0:
			feeling-1
	for i in range(0,len(boundaries[1])-1):
		pos = data.find(boundaries[1][i])
		if pos < 0:
			feeling+1

	#clearing every thing out
	
	
	dataSplit = data.split(" ")
	
	noHigh = 1
	
	#check database for known replys
	for i, item in enumerate(inMessage):
		splitBuffer = []
		splitBuffer = inMessage[i].split(" ")
		wordMatch[i] = 0
		for h, item in enumerate(splitBuffer):
			for g, item in enumerate(dataSplit):
				
				if dataSplit[g] == splitBuffer[h]:
					wordMatch[i] = wordMatch[i] + 4
					match = 1
			if match == 0:
				wordMatch[i] = wordMatch[i] - 1
			match = 0
#may be causeing miss readings
			
				
			
		if wordMatch[i] > 0:
			noHigh = 0
	
	for i, item in enumerate(inMessage):
		if wordMatch[highWord] < wordMatch[i]:
			highWord = i
			
	if debug == 1:		
		print wordMatch
		print inMessage[highWord]
			
	if done != 2:
		if(noHigh == 1):
			done = 0
		else:
			done = 1		


			temp = []
			
			for k, item in enumerate(inMessage):
				if inMessage[k] == inMessage[highWord]:
					temp.append(k)
					
			message = outMessage[temp[random.randint(0,(len(temp)-1))]]
			message = string.replace(message,"/AGE",str(age))
			message = string.replace(message,"/NAME",namel)
			message = string.replace(message,"/UNAME",usersnamel)
			message = string.replace(message,"/LNAME",lname)
			message = string.replace(message,"/FNAME",fname)
			if (feeling > 5):
				feeling = 5
			if (feeling < 0):
				feeling = 0
			message = string.replace(message,"/FEEL",feelings[feeling][random.randint(0,len(feelings[feeling])-1)])

	if done == 0:
	
		reply = raw_input("Sorry I don't know how to reply please enter: ")
		inMessage.append(data)
		outMessage.append(reply)
		wordMatch.append(0)
		
	elif done == 1:

		now = time.strftime("%H:%M:%S")
		print now + " " + namel + ": " + message
		
	chats = chats + 1
	done = 0
	
	if chats == 10:
		print "saving"
		
		
		saveData(inMessage, outMessage, usernamel)
		
		chats = 0
