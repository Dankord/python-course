# John Kervin M. Ganzon

#Installment 1
print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print("\nWelcome! This is your personal expense tracker.\n")
print("MAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)")

# Installment 3
name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
subtotal = 0

firstExpense = input("\nFirst Expense? ")
amount1 = float(input("Amount? "))

subtotal+=amount1

secondExpense = input("Second Expense? ")
amount2 = float(input("Amount? "))

subtotal+=amount2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax
over_budget = total > budget
left = budget - total

print("-" * 40)
print("SUMMARY")
print(f"\t- {firstExpense}:\t${amount1}")
print(f"\t- {secondExpense}:\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${subtotal / 2}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand total:\t\t${total}")
print(f"Over budget?\t\t{over_budget}")
print(f"Left in the budget:\t${left}")
print("-" * 40)
print("Made by: John Kervin M. Ganzon | Installment 3")