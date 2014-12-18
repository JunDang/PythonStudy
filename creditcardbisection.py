def CreditCard(balance, AnnualInterestRate):
	MonthlyInterestRate= (AnnualInterestRate) / 12.0
	MonthlyPaymentLow = balance / 12
	MonthlyPaymentHigh = balance*(1 + MonthlyInterestRate)**12 / 12.0
	MinimumMonthlyPayment = (MonthlyPaymentLow + MonthlyPaymentHigh) / 2
	epsilon = 0.01
	while True: 
		currentBalance = balance
		for i in range(12):
			currentBalance = (currentBalance - MinimumMonthlyPayment) * (1 + MonthlyInterestRate)
		if abs(currentBalance) > epsilon:
			if (currentBalance < -epsilon):
				MonthlyPaymentHigh = MinimumMonthlyPayment
			else:
				MonthlyPaymentLow = MinimumMonthlyPayment
			MinimumMonthlyPayment = (MonthlyPaymentLow + MonthlyPaymentHigh) / 2
		else:
			break
	print 'lowest payment: ' + str(MinimumMonthlyPayment)
	print 'Remaining balance: ' + str(currentBalance)
CreditCard(320000, 0.2)



