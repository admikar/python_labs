# # Банкир.
#
# # Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# # Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# # Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.
#
# # Напишите тут ваш код
# class BankAccount:
#     def __init__(self, account_number, initial_balance):
#         self.account_number = account_number
#         self.initial_balance = initial_balance
#
#     def deposit(self, amount):
#         self.initial_balance += amount
#         print(self.initial_balance)
#
#     def withdraw(self, amount):
#         if self.initial_balance >= amount:
#             self.initial_balance -= amount
#         else:
#             print("NOt enough money")
#         print(self.initial_balance)
#
# account = BankAccount(12345, 100)
# account.deposit(100)
# account.deposit(100)
# account.withdraw(400)
# account.deposit(100)
# account.withdraw(400)
#
#

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and not exceed the current balance.")

# Создание аккаунта и операции по нему
account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
account.deposit(300)
account.withdraw(700)
account.withdraw(1000)