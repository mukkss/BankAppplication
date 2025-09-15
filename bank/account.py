from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_num: str, balance: float = 0.0):
        self._account_num = account_num    # private-like
        self._balance = balance            # private-like

    @property
    def account_num(self) -> str:
        return self._account_num

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        print(f"[INFO] Deposited {amount}. New Balance: {self._balance}")
        return self._balance

    @abstractmethod
    def withdraw(self, amount: float) -> float:
        pass

    def __str__(self):
        return f"Account[{self.account_num}] Balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_num: str, balance: float = 0.0, interest_rate: float = 0.03):
        super().__init__(account_num, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise ValueError("Insufficient funds in Savings Account")
        self._balance -= amount
        print(f"[INFO] Withdrew {amount}. New Balance: {self._balance}")
        return self._balance

    def calculate_interest(self) -> float:
        interest = self.balance * self.interest_rate
        print(f"[INFO] Interest: {interest}")
        return interest


class CurrentAccount(Account):
    def __init__(self, account_num: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(account_num, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> float:
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit")
        self._balance -= amount
        print(f"[INFO] Withdrew {amount}. New Balance: {self._balance}")
        return self._balance
