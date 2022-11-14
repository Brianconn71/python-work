numOfHours = int(input("Enter hours worked this week: "))
hourlyRate = float(input("Enter hourly rate of pay: "))

if 0 <= numOfHours <= 35:
    weeklyPay = float(numOfHours * hourlyRate)
    print(f"Weekly pay is {weeklyPay:.2f}")
elif numOfHours > 35:
    weeklyPay = float(35 * hourlyRate + (numOfHours - 35) * hourlyRate * 1.5)
    print(f"Weekly pay is {weeklyPay:.2f}")