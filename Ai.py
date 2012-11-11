import json
import random
import time
import datetime
import string

def saveData(inArray, outArray):
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
	
	store = '{' + store1 + ',' + store2 + '}'

	fileJson = open("data/brain.json", "w")
	fileJson.write(store)
	fileJson.close()

firstnames = ["Mark","Ben","Tom","Tim","George","Lily","Megan","Linus","Abbie","Elizabeth","Ryan"] #MORE NAMES!
lastnames = ["Smith","Johnson","Williams","Jones","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson","Thomas"]

lname = lastnames[random.randint(0,len(lastnames)-1)]
fname = firstnames[random.randint(0,len(firstnames)-1)]

namel = fname+" "+lname
age = random.randint(14,60)

print "waking up..."


now = datetime.datetime.now()

usersnamel = raw_input(str("%02d" %(now.hour))+":"+str("%02d" %(now.minute))+":"+str("%02d" %(now.second))+" "+namel+": What is your name?\n"+str("%02d" %(now.hour))+":"+str("%02d" %(now.minute))+":"+str("%02d" %(now.second))+" You: ")
message = "Hello "+usersnamel
inMessage = []
outMessage = []
feelings = []

data = ""
dataSplit = []
splitBuffer = []

wordMatch = []
highWord = 0
noHigh = 1

done = 0

debug = 1

chats = 0

running = 1

olddata = "Hello"

#loading and processing json file
jsonFile = open('data/brain.json').read()

#print jsonFile

brain = json.loads(jsonFile)

for i, item in enumerate(brain["inData"]):
	inMessage.append(brain["inData"][i]["id"])
	outMessage.append(brain["outData"][i]["id"])
	wordMatch.append(0)

print len(brain["inData"])

now = datetime.datetime.now()

print str("%02d" %(now.hour))+":"+str("%02d" %(now.minute))+":"+str("%02d" %(now.second))+" "+namel+": "+message

while running == 1:
	
	data = raw_input(str("%02d" %(now.hour))+":"+str("%02d" %(now.minute))+":"+str("%02d" %(now.second))+" "+usersnamel+": ")
	
	#commands
	if data == "*LIST":
		for i, item in enumerate(inMessage):
			print inMessage[i], ", ", outMessage[i]
		done = 2
		
	if data == "*SAVE":
		print "saving"
		
		saveData(inMessage, outMessage)
		
		done = 2
	
	if data == "*EXIT":
		now = datetime.datetime.now()
		print str("%02d" %(now.hour))+":"+str("%02d" %(now.minute))+":"+str("%02d" %(now.second))+" "+namel+": Bye see you soon"

		
		print "saving"
		
		saveData(inMessage, outMessage)
		
		done = 2
		running = 0
	if data == "*THINK":
		q = random.randint(0,(len(inMessage)-1))
		now = datetime.datetime.now()
		p = raw_input(str("%02d" %(now.hour))+":"+str("%02d" %(now.minute))+":"+str("%02d" %(now.second))+" "+namel+": "+inMessage[q]+"\nYou: ")
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
					wordMatch[i] = wordMatch[i] + 2
				else:
					if wordMatch[i] > 0:
						wordMatch[i] = wordMatch[i] - 1
				
			
		if wordMatch[i] > 0:
			noHigh = 0
	if debug == 1:		
		print wordMatch
	
	for i, item in enumerate(inMessage):
		if wordMatch[highWord] < wordMatch[i]:
			highWord = i
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

	if done == 0:
		reply = raw_input("Sorry I don't know how to reply please enter: ")
		inMessage.append(data)
		outMessage.append(reply)
		wordMatch.append(0)
	elif done == 1:

		now = datetime.datetime.now()
		print str("%02d" %(now.hour))+":"+str("%02d" %(now.minute))+":"+str("%02d" %(now.second,))+" "+namel+": "+ message
	chats = chats + 1
	done = 0
	
	if chats == 10:
		print "saving"
		
		
		store1 = '"inData":['
		for i, item in enumerate(inMessage):
			if(i == (len(inMessage)-1)):
				store1 = store1 + '{"id":"' + str(inMessage[i]) + '"}'
			else:
				store1 = store1 + '{"id":"' + str(inMessage[i]) + '"},'
		
		store1 = store1 + ']'
		
		store2 = '"outData":['
		for i, item in enumerate(outMessage):
			if(i == (len(inMessage)-1)):
				store2 = store2 + '{"id":"' + str(outMessage[i]) + '"}'
			else:
				store2 = store2 + '{"id":"' + str(outMessage[i]) + '"},'
		
		store2 = store2 + ']'
		
		store = '{' + store1 + ',' + store2 + '}'

		fileJson = open("data/brain.json", "w")
		fileJson.write(store)
		fileJson.close()
		
		chats = 0
