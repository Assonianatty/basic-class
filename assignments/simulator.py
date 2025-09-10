def atm_simulator():
    balance = 1000  # Starting balance

    while True:
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your current balance is: ${balance}")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                if amount <= 0:
                    print("Deposit amount must be greater than zero.")
                else:
                    balance += amount
                    print(f"Deposit successful! New balance: ${balance}")
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                if amount <= 0:
                    print("Withdrawal amount must be greater than zero.")
                elif amount > balance:
                    print("Insufficient funds!")
                else:
                    balance -= amount
                    print(f"Transaction successful! New balance: ${balance}")
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

# Run the ATM program
atm_simulator()