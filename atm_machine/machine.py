class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. New Balance: {self.balance}"
        return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        elif amount <= 0:
            return "Withdrawal amount must be greater than zero."
        else:
            self.balance -= amount
            return f"Withdrew: {amount}. New Balance: {self.balance}"

    def check_balance(self):
        return f"Current Balance: {self.balance}"


