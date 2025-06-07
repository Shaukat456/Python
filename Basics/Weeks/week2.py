# Assignment: Week 2 - Python Basics

# Check if a number is divisible by 3 or not

# Check if a year is greater than 2020 (future year)

# Check if a character is a vowel

# Ask name, print greeting only if it’s not empty

# Temperature check → hot, cold, or normal


# Grade student based on 5-subject average

# Ask username and password → check both

# Ask a number → print if it’s prime or not

# Create login system with retry message


#  Compare two numbers and print which one is larger or if they are equal
#  Input: two numbers
# Output: which one is larger or if they are equal


# Ask for 2 numbers and an operator (+, -, *, /)
# Perform the operation based on user choice


# # Input: units
# 1-100 units: Rs. 5/unit
# 101-200 units: Rs. 7/unit
# 200+ units: Rs. 10/unit
# Print the total bill


# . Find the Greatest of 3 Numbers
# # Use only if-elif-else (no max())


#  ATM Withdrawal with Conditions
# Input: amount, check if it’s divisible by 500 and ≤ balance


#  Mini ATM Project
# Initial values
correct_pin = "1234"
balance = 5000
is_verified = True

# Step 1: Ask for PIN
pin = input("Enter your 4-digit PIN: ")

if pin == correct_pin:
    print("\n✅ Login successful!\n")

    while True:
        print("=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"\n💰 Your balance is: Rs. {balance}\n")

        elif choice == "2":
            if not is_verified:
                print("❌ You must verify your account to withdraw money.\n")
            else:
                amount = float(input("Enter amount to withdraw: Rs. "))
                if amount <= 0:
                    print("❌ Enter a valid amount.\n")
                elif amount > 3000:
                    print("❌ Withdrawal limit is Rs. 3000 per transaction.\n")
                elif amount > balance:
                    print("❌ Insufficient funds.\n")
                else:
                    balance -= amount
                    print(f"✅ Withdrawal successful! New balance: Rs. {balance}\n")

        elif choice == "3":
            amount = float(input("Enter amount to deposit: Rs. "))
            if amount <= 0:
                print("❌ You cannot deposit zero or negative money.\n")
            else:
                balance += amount
                print(f"✅ Deposit successful! New balance: Rs. {balance}\n")

        elif choice == "4":
            print("👋 Thank you for using the ATM. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select from the menu.\n")
else:
    print("❌ Incorrect PIN. Access denied!")
