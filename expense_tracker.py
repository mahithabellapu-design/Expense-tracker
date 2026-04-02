# Expense Tracker (Fixed Version)

expenses = []   # <-- defined ONCE here

def add_expense(amount):
    expenses.append(amount)

def show_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("Expenses:", expenses)

def total_expense():
    print("Total Expense:", sum(expenses))

# Main program
print("Expense Tracker")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Enter expense amount: "))
        add_expense(amount)

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
