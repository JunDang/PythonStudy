class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
def toString(atMe):
	namelist = [atMe.myName()]
	itembefore = atMe
	while True:
		itembefore = itembefore.getBefore()
		if itembefore is None:
			break
		else:
			namelist.insert(0, itembefore.myName())
	itemafter = atMe
	while True:
		itemafter = itemafter.getAfter()
		if itemafter is None:
			break
		else:
			namelist.append(itemafter.myName())
	return " = ".join(namelist)	
def insert(atMe, newFrob):
	"""
	atMe: a Frob that is part of a doubly linked list
	newFrob:  a Frob with no links?
	This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
	"""
	# Your Code Here
	me = atMe.myName()
	new = newFrob.myName()
	item = atMe
	if me == new:
		newFrob.setBefore(atMe.getBefore())		
		newFrob.setAfter(atMe)
		atMe.getBefore().setAfter(newFrob)
		atMe.setBefore(newFrob)
	elif me > new:		
		while True:
			if item.getBefore() is None or new > item.getBefore().name:
				break
			item = item.getBefore()
		
		#print item.name
		if item.getBefore() is None:
			item.setBefore(newFrob)
			newFrob.setAfter(item)
		else:
			item.getBefore().setAfter(newFrob)
			newFrob.setBefore(item.getBefore())
			newFrob.setAfter(item)
			item.setBefore(newFrob)
		
	else:		
		while True:
			if item.getAfter() is None or new < item.getAfter().name:
				break
			item = item.getAfter()
		if item.getAfter() is None:
			item.setAfter(newFrob)
			newFrob.setBefore(item)
		else:
			item.getAfter().setBefore(newFrob)
			newFrob.setAfter(item.getAfter())
			newFrob.setBefore(item)
			item.setAfter(newFrob)
				

def findFront(start):
	"""
	start: a Frob that is part of a doubly linked list
	returns: the Frob at the beginning of the linked list 
	"""
	# Your Code Here
	
	if start.getBefore() is None:
		return start
	else:
		return findFront(start.getBefore())
			
				
				
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
eric.setBefore(andrew)
andrew.setAfter(eric)
eric.setAfter(fred)
fred.setBefore(eric)
fred.setAfter(martha)
martha.setBefore(fred)
martha.setAfter(ruth)
ruth.setBefore(martha)
martha1 = Frob('martha')
#eric2 = Frob('eric')
#insert(eric, eric2)
#insert(eric, fred)
insert(fred, martha1)
print toString(eric)				
			
				