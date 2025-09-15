from bank.bank import Bank

def main():
    my_bank = Bank("Lakshya Bank")

    # Add a customer with details
    mukesh = my_bank.add_customer("CUST001", "Mukesh", 21, "M", "mukesh@example.com")

    # Open accounts
    savings = my_bank.open_account(mukesh, "savings", "ACC1001", 1000)
    current = my_bank.open_account(mukesh, "current", "ACC1002", 500)

    # Perform transactions
    savings.deposit(500)
    savings.calculate_interest()
    current.withdraw(200)

    # List customers
    my_bank.list_customers()

if __name__ == "__main__":
    main()
