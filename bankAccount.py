class BankAccount:
    def __init__(self, account_type, amount):
        self.account_type = account_type
        self.amount = amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        self.amount -= withdraw_amount

    def __str__(self):
        return "{} : {}".format(self.account_type, self.amount)
qazi = BankAccount("Checkings", 100)
qazi.deposit(100)
qazi.withdraw(30)
print(qazi)
# print(str(qazi.account_type) + ":" + str(qazi.amount))
