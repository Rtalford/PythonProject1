import os
import pandas as pandas

class BankAccount:
  

  # Init Function
  def __init__(self, owner, balance=0):
      self.owner = owner
      self.balance = balance
      self.transactions = []
   

  # # __str__
  def __str__(self):
     return f'Owner: {self.owner}\nOpening Balance: {self.balance}'
      

  # deposit_funds()
  def deposit_funds(self, amount):
     t = {'owner': self.owner, 'type': 'deposit', 'amount': {amount}}
     self.transactions.append(t)
     return self.transactions


  # # withdraw_funds()
  def withdraw_funds(self, amount):
     deposits = sum(s['amount'] for s in self.transactions if s['type'] == 'deposit')
     total_balance = deposits +  self.balance

     if total_balance < amount:
        print("Insufficent funds")
     else: 
         t = {'owner': self.owner, 'type': 'withdrawal', 'amount': {amount}}
         self.transactions.append(t)
         print(self.transactions)

     print(f'My Deposits are {deposits} and my inital balance is 
     {total_balance}')
  
     
     
   


  # # get_balance()
  # def get_balance(self):
  #   pass

  # # get_transactions()
  # def get_transactions(self):
  #   pass

  # # transaction_count()
  # def transaction_count(self):
  #   pass

  # # transaction_history()
  # def transaction_history(self):
  #   pass

  # # save_transaction()
  # def save_transaction(self):
  #   pass
      
    
# Create my class instance 
Florence_account = BankAccount('Florence', 4000)


# testing __str__
# print(Florence_account)

#testing deposit
Florence_account.deposit_funds(50)
Florence_account.deposit_funds(200)

#testing withdrawals

Florence_account.withdraw_funds(25)
Florence_account.withdraw_funds(50)
Florence_account.withdraw_funds(5000)