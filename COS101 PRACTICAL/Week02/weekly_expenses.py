# Student Weekly Expense Calculator
# Collects a student's weekly costs and displays a summary.

# INPUT
student_name = input("Enter the student's name: ")
daily_transport = float(input("Enter the daily transport cost in naira: "))
daily_feeding = float(input("Enter the daily feeding cost in naira: "))
days_on_campus = int(input("Enter the number of days on campus: "))
other_expenses = float(input("Enter the other expenses for the week in naira: "))

# PROCESS
transport_total = daily_transport * days_on_campus
feeding_total = daily_feeding * days_on_campus
weekly_total = transport_total + feeding_total + other_expenses

# OUTPUT
print()
print("WEEKLY EXPENSE SUMMARY")
print(f"Student: {student_name}")
print(f"Transport total: NGN {transport_total:,.2f}")
print(f"Feeding total: NGN {feeding_total:,.2f}")
print(f"Other expenses: NGN {other_expenses:,.2f}")
print(f"Weekly total: NGN {weekly_total:,.2f}")
