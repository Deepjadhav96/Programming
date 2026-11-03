
class BankAccount:
   ROI = 10.5
   def __init__(self,CustName):
       self.Name = CustName
       self.Balance = 1000 #Fixed deposite for creating account
   
   def Display(self):
       print(f"Customer Name : {self.Name}")
       print(f"Customer Balance : {self.Balance}")

   def Deposite(self,CustBalance):
       self.Total = self.Balance + CustBalance
       return self.Total
   
   def WithDraw(self,MoneyWithdraw):
       if self.Total > 1000:
           self.Total = self.Total - MoneyWithdraw
       return self.Total
           
   def CalculateInterest(self):
       Interest = (self.Total * BankAccount.ROI) / 100
       return Interest
        
    
def main():
    Name = input("Enter a Name")
    bobj = BankAccount(Name)

    print(bobj.Display())
    print(bobj.Deposite(1000))
    print(bobj.WithDraw(100))
    print(bobj.CalculateInterest())

if __name__ == "__main__":
    main()