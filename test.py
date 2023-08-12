class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount

    def withdraw(self, amount):
        self.initial_balance -= amount

    def display_balance(self):
        print(f"Номер вашего счета: {self.account_number} "
              f"Количество деняк: {self.initial_balance}")

akbars = BankAccount(4)
akbars.deposit(400)
akbars.display_balance()
akbars.withdraw(200)
akbars.display_balance()
