monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
savings = monthly_income-monthly_expenses
air = 5
projected_savings = int(savings*12+(savings*12*0.05))
print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
