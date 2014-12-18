      
def FancyDivide(list_of_numbers, index):
	denom = list_of_numbers[index]
	return [SimpleDivide(item, denom)
			for item in list_of_numbers]
			   
def SimpleDivide(item, denom):
	try: 
		return item / denom    
	except ZeroDivisionError, e:
		return 0

#change the definition of SimpleDivide so that the call does not raise an exception. When dividing by 0, FancyDivide should return a list with all 0 elements. 