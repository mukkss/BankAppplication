class Customer:
    def __init__(self, customer_id: str, name: str, age: int, gender: str, contact_info: str):
        self._customer_id = customer_id  # fixed recursion issue
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info
        self._accounts = []

    @property
    def customer_id(self) -> str:
        return self._customer_id

    def add_account(self, account) -> None:
        self._accounts.append(account)
        print(f"[INFO] Added {account} for {self.name}")

    def get_accounts(self):
        return self._accounts

    def get_account(self, account_num: str):
        for account in self._accounts:
            if account.account_num == account_num:
                return account
        return None

    def __str__(self):
        return f"Customer[{self.customer_id}] {self.name} ({self.gender}, {self.age} yrs)"
