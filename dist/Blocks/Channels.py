# Module detail:
# This file describes the Channel GUI class
# Objects of such class have the following attributes:
# This file also contains the tests for the Block module
class Channel:
	def __init__(self,id,source,destination,argN=None):
		self.ID=id;
		self.SourceID=source
		self.DestinationID=destination
		self.ArgN=argN
		#self.Data=data;
	def changeSourceID(self,source):
		self.SourceID=source
	def changeDestinationID(self,destination):
		self.DestinationID=destination
	def In(self,data):
		self.Data=data
	def Out(self):
		return self.Data

def FindSrc(Clist,Blist,name,id,argN=None): #we are destination
	result = []
	for i in Clist:
		if i.DestinationID.Name == name and i.DestinationID.ID == id:
			for j in Blist:
				if j.Name == i.SourceID.Name and j.ID == i.SourceID.ID:
					if argN != None:
						if(argN == i.ArgN):
							result.append(j)
						else:
							print("FindSrc: "+str(argN)+", " +str(i.ArgN))
					else:
						result.append(j)
	return result
def FindDst(Clist,Blist,name,id,argN=None): #we are destination
	result = []
	for i in Clist:
		if i.SourceID.Name == name and i.SourceID.ID == id:
			for j in Blist:
				if j.Name == i.DestinationID.Name and j.ID == i.DestinationID.ID:
					if argN != None:
						if(argN == i.ArgN):
							result.append(j)
						else:
							pass
					else:
						result.append(j)
	return result
def testCase():
	import random
	print("Test case:")
	source=random.randint(1, 10)
	destination=random.randint(1, 10)
	data=random.randint(1,10)
	print("Source ID is: "+str(source)+".")
	print("Destination ID is: "+str(destination)+".")
	#print("Data is: "+str(data)+".")
	C_ab=Channel(0,source,destination)
	if (C_ab.SourceID == source):
		print("initial self.SourceID: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("initial self.SourceID: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (C_ab.DestinationID == destination):
		print("initial self.DestinationID: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("initial self.DestinationID: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	#if (C_ab.Data == data):
	#	print("initial self.Data: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	#else:
	#	print("initial self.Data: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	print("___")
	print("Testing the change functions")
	C_ab.changeSourceID(random.randint(11, 100))
	if (C_ab.SourceID != source):
		print("self.SourceID: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.SourceID: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	C_ab.changeDestinationID(random.randint(11, 100))
	if (C_ab.DestinationID != destination):
		print("self.DestinationID: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.DestinationID: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	print("___")
	print("Testing the functionality")
	newData=random.randint(11, 100)
	C_ab.In(newData)
	if (C_ab.Data != data):
		print("self.In(): "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.In(): "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	print("New data is: "+str(C_ab.Out())+".")
	if (C_ab.Out() == newData):
		print("self.Out(): "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Out(): "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
testCase()
