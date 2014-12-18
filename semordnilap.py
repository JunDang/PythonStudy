def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    if len(str1) != len(str2):
        return False
    elif str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-2])
    else:
		return False
print semordnilap("hello", "0000h")