def genPrimesFn():
    '''Function to keep printing the prime number until the user stops the program.
    This way uses user input; you can also just run an infinite loop (while True)
    that the user can quit out of by hitting control-c'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    uinp = 'y'    # Assume we want to at least print the first prime...
    while uinp != 'n':
        last += 1
        for p in primes:
            if last % p == 0:
                break
            else:
                primes.append(last)
                print last
                uinp = raw_input("Print the next prime? [y/n] ")
                while uinp != 'y' and uinp != 'n':
                    #while uinp
                    print "Sorry, I did not understand your input. Please enter 'y' for yes, or 'n' for no."
                    uinp = raw_input("Print the next prime? [y/n] ")
                if uinp == 'n':
                    break
genPrimesFn()
