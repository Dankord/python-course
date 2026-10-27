# John Kervin M. Ganzon

expenses = []
subtotal = 0

# Banner
print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print("\nWelcome! This is your personal expense tracker.\n")
name = input("\nWhat's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

# Loop
while True:
    #Installment 1
    print("MAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses\t\t(coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")

    choice = int(input("Choose 1-4: "))
    # Installment 3

    if choice == 1:
        # Expense = input("\nFirst Expense? ")
        amount = float(input("Amount? "))

        # Installment 4
        if amount > 200:
            print("\tHuge Expense - are you sure?")
        elif amount > 100:
            print("\tBig Expense.")
        elif amount > 50:
            print("\tModerate Expense.")
        else:
            print("\tSmall expense.")

        expenses.append(amount)
        subtotal+=amount

    elif choice == 2:
        print("\tComing Soon: the tracker can't remember each item yet.\n")

    elif choice == 3:
        tax = subtotal * (tax_percent / 100)

        total = subtotal + tax
        over_budget = total - budget
        left = budget - total

        print("-" * 40)
        print("SUMMARY")
        print(f"Expenses:\t\t{len(expenses)}")
        print(f"Subtotal:\t\t${subtotal}")
        # print(f"Average:\t\t${subtotal / 2}")
        print(f"Tax ({tax_percent}%):\t\t${tax}")
        print(f"Grand total:\t\t${total}")

        # Installment 4
        if total > budget:
            print(f"Over budget by ${over_budget}!")
        elif total > budget * 0.90:
            print(f"Careful: only ${left} left.")
        else:
            print(f"Within budget: ${left} left.")

    elif choice == 4:
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: John Kervin M. Ganzon | Installment 5")
        break
    else:
        print("\tPlease choose 1, 2, 3, or 4.")
