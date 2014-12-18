def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    count = 0
    for c in aStr:
        count = count + 1
    return count
	
recursive method
def lenRecur(aStr):
	if aStr == ' ':
		return 0
	else:
		return 1 + lenRecur(aStr[1:]
		