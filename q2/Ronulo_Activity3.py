
class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("The balance must be not a negative number.")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance


a1 = BankAccount(12345, 1000)

print("Object of class BankAccount")
print()
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

print()
print("Update balance to -100")
a1.balance = -100

print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance}")
