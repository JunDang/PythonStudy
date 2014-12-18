def CreditCard(balance, AnnualInterestRate):
	MonthlyInterestRate= (AnnualInterestRate) / 12.0
	MonthlyPaymentLow = balance / 12
	MonthlyPaymentHigh = balance*(1 + MonthlyInterestRate)**12 / 12.0
	while True: 
		currentBalance = balance
		MinimumMonthlyPayment = (MonthlyPaymentLow + MonthlyPaymentHigh) / 2
		for i in range(12):
			currentBalance = (currentBalance - MinimumMonthlyPayment) * (1 + MonthlyInterestRate)
		if (abs(currentBalance) <= 0.01):
			break
		else:
			if currentBalance > 0.01:
				MonthlyPaymentLow = MinimumMonthlyPayment
			else:
				MonthlyPaymentHigh = MinimumMonthlyPayment
	print 'lowest payment: ' + str(MinimumMonthlyPayment)
	print 'Remaining balance: ' + str(currentBalance)
CreditCard(320000, 0.2)



