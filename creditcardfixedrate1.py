def CreditCard(balance, AnnualInterestRate):
	MonthlyInterestRate= (AnnualInterestRate) / 12.0
	MinimumMonthlyPayment = 0
	for monthlyPayment in range(10, balance, 10):
		curBalance = balance
		for i in range(12):
			curBalance = (curBalance - monthlyPayment) * (1 + MonthlyInterestRate)
		if curBalance < 0:
			MinimumMonthlyPayment = monthlyPayment
			break;
	print 'Lowest Payment: ' + str(MinimumMonthlyPayment)
CreditCard(3329, 0.2)		
CreditCard(4773, 0.2)
CreditCard(3926, 0.2)

