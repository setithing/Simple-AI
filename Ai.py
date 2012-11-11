import json

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


print "waking up..."

message = "Hello world"

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

chats = 0

running = 1

#loading and processing json file
jsonFile = open('data/brain.json').read()

#print jsonFile

brain = json.loads(jsonFile)

for i, item in enumerate(brain["inData"]):
	inMessage.append(brain["inData"][i]["id"])
	outMessage.append(brain["outData"][i]["id"])
	wordMatch.append(0)

print len(brain["inData"])

print "Computer: ", message

while running == 1:
	
	data = raw_input("You: ")
	
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
		print "Computer: Bye see you soon"
		
		print "saving"
		
		saveData(inMessage, outMessage)
		
		done = 2
		running = 0
		
	if data == "thats not right":
	
		a = raw_input("Sorry did I get it wrong (Y/N): ")
		
		if a == "Y"
		
	#end of commands
	
	#string checking
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
					
		if wordMatch[i] > 0:
			noHigh = 0
			
		if wordMatch[i] < int(wordMatch[i]*0.80):
			wordMatch[i] = 0
			
	print wordMatch
	
	for i, item in enumerate(inMessage):
		if wordMatch[highWord] < wordMatch[i]:
			highWord = i
	if done != 2:
		if(noHigh == 1):
			done = 0
		else:
			done = 1		
			print "Best match: ", inMessage[highWord]
			print "Best reply: ", outMessage[highWord]
			message = outMessage[highWord]

	if done == 0:
		reply = raw_input("Sorry I don't know how to reply please enter: ")
		inMessage.append(data)
		outMessage.append(reply)
		wordMatch.append(0)
	elif done == 1:
		print "Computer: ", message
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
