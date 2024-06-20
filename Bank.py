#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account.

class BankAccount:
  def __init__(self, account_number, balance: int):
    self.account_number = account_number
    self.balance = balance

  def deposit(self):
    self.balance = self.balance + deposit_amount
  def withdraw(self):
    self.balance = self.balance - withdraw_amount
  #def change_age(self):
#         self.age = self.age + self.age_increase_amount
  #def withdraw(self):
    #self.balance -= withdraw_amount

   # else:
      #print("Insufficient funds")

account1 = BankAccount(12121212, 200)
print(account1.balance, account1.account_number)


withdraw_deposit = input("Do you want to withdraw or deposit? ")
if withdraw_deposit == "withdraw":
      deposit_amount = int(input("Enter amount to deposit: "))
elif withdraw_deposit == "deposit":
      withdraw_amount = int(input("Enter amount to withdraw: "))
account1.deposit()
print(account1.balance)


    