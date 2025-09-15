from .customers import Customer
from .account import SavingsAccount, CurrentAccount

class Bank:
    def __init__(self, name: str):
        self.name = name
        self._customers = {}

    def add_customer(self, customer_id: str, name: str, age: int, gender: str, contact_info: str):
        if customer_id in self._customers:
            raise ValueError(f"Customer with ID {customer_id} already exists.")
        customer = Customer(customer_id, name, age, gender, contact_info)
        self._customers[customer_id] = customer
        print(f"[INFO] Added customer {customer}")
        return customer

    def open_account(self, customer: Customer, account_type: str, account_number: str, initial_balance: float = 0):
        if account_type == "savings":
            account = SavingsAccount(account_number, initial_balance)
        elif account_type == "current":
            account = CurrentAccount(account_number, initial_balance)
        else:
            raise ValueError("Invalid account type. Choose 'savings' or 'current'.")
        customer.add_account(account)
        return account

    def get_customer(self, customer_id: str):
        return self._customers.get(customer_id)

    def list_customers(self):
        for cust in self._customers.values():
            print(cust)
