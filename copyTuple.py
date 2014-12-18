def oddTuples(aTup):
	cList = []
	copyList = []
	cTup = ()
	#for i in aTup:
	#	cList = cList + [i,]
	cList = list(aTup)
	print cList
	for j in cList:
		if cList.index(j) % 2 == 0:  #if there are 2 euqal elements, only return the index of the first element. so it is wrong. 
			copyList = copyList + [j,]
	print copyList
	#for m in copyList:
	#	cTup = cTup + (m, )
	cTup = tuple(copyList)
	return cTup
print oddTuples(('I', 'am', 'a', 'test', 'tuple'))

right version:
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    cList = []
    copyList = []
    cTup = ()
    cList = list(aTup)
    for j in range(len(cList)):
        if j % 2 == 0:
            copyList = copyList + [cList[j]]
    cTup = tuple(copyList)
    return cTup
	
def oddTuples2(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to 
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup

def oddTuples3(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    # Here is another solution to the problem that uses tuple 
    #  slicing by 2 to achieve the same result
    return aTup[::2]