def CreditCard(balance, AnnualInterestRate):
	MonthlyInterestRate= (AnnualInterestRate) / 12.0
	MinimumMonthlyPayment = 0
	while True: 
		currentBalance = balance
		MinimumMonthlyPayment += 10 
		for i in range(12):
			currentBalance = (currentBalance - MinimumMonthlyPayment) * (1 + MonthlyInterestRate)
		if (currentBalance < 0):
			break
	print 'lowest payment: ' + str(MinimumMonthlyPayment)
	print 'Remaining balance: ' + str(currentBalance)
CreditCard(3926, 0.2)		

