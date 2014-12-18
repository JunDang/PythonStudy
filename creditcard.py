def CreditBalance(balance, MinMonthlyPaymentRate, AnnualInterestRate):
	MonthlyInterestRate= (AnnualInterestRate) / 12.0
	totalPaid = 0
	for i in range(12):
		print "Month: " + str(i+1)
		MinimumMonthlyPayment = (MinMonthlyPaymentRate) * balance
		totalPaid = totalPaid + MinimumMonthlyPayment
		print "Minimum monthly payment: " + str(MinimumMonthlyPayment)
		unpaidBalance = balance - MinimumMonthlyPayment
		balance = unpaidBalance + MonthlyInterestRate* unpaidBalance
		print "Remaining balance: " + str(balance)
	print 'Total paid: ' + str(totalPaid)
	print 'Remaining balance: ' + str(balance)
CreditBalance(4213, 0.04, 0.2)	
