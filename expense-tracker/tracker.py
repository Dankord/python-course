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
print("-" * 40)
print("Made by: John Kervin M. Ganzon | Installment 1")
print("=" * 40)

# Installment 2
name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

firstExpense = input("\nFirst Expense? ")
amount1 = float(input("Amount? "))

secondExpense = input("Second Expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2

print("-" * 40)
print("SUMMARY")
print(f"\t- {firstExpense}:\t${amount1}")
print(f"\t- {secondExpense}:\t${amount2}")
print(f"Total spent:\t\t${total}")
print(f"Average:\t\t${total / 2}")
print("-" * 40)
print("Made by: John Kervin M. Ganzon | Installment 2")