
``` python
class  BankAccount:
    
    
           def  __init__ (self , account_number , balance):
               
                   self.account_number = account_number
                   self.balance = balance
                   
                   
                   
           def  deposit (self , amount):
               
                 if amount > 0  :
                     
                   self.balance += amount
                   print(f"amount:{amount} credited to the account {self.account_number} successfully.")
                   
                 else:
                        print("Deposit amount must be greater than zero.")
                        
                        
                        
           def  withdraw (self , amount):
               
                  if self.balance  > 0 :
                         self.balance -= amount  
                         print(f"amount:{amount} is debited from account:{self.account_number} succesfully.")
                  else:
                         print("Insufficient balance. Withdrawal not allowed.")  
                         
                         
                         
           def  check_balance (self) :
                  print(f"balance in a account:{self.account_number} is {self.balance}. ")
                
customer_1 = BankAccount(125638234,200)
customer_2 = BankAccount(678573643,5000)


customers={"customer_1":customer_1 , "customer_2":customer_2}

while True :
    
  customer_input  = input("\nMention :customer_1 / customer_2:")
  customer = customers.get(customer_input)
    
  if customer is None:
        print("Invalid customer name.")
        continue

  choice  = int(input("\n enter your choice for operation \n 1:deposit.\n 2: withdraw .\n 3: chech balance.\n"))
  
  match choice:
       case 1:
              amount = int(input("enter a money to credit:"))
              customer.deposit(amount)
       case 2:
              amount = int(input("enter a amount to withdraw:") )
              customer.withdraw(amount)
       case 3:
              customer.check_balance()
       case _  : print("enter a valid choice:")          
```
