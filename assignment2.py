"""
ASSIGNMENT 2: Design a ATM Simulator using OOPS 
"""
import random

class ATM:
    userName = "tharunbalaji31"
    passWord = "tharun@123"
    balance = 20000
    otp = ''

    def __init__(self,userName,passWord) -> None:
        if (self.userName == userName and self.passWord == passWord):
            print("\n<------ LOGIN SUCCESSFUL ------>\n")
            self.dashBoard(userName)
        else:
            print("<------ LOGIN FAILED ------>")
            print("Invalid Username or Password\n")

    def dashBoard(self,userName) -> str:
        print(f"Welcome {userName}\n")
        
        while (True):
            print("1.Balance\n2.Withdrawl\n3.Deposit\n4.Exit")
            option = int(input("Choose your option: "))

            self.generateOTP()
            user_otp = int(input("Enter your OTP: "))
            res = self.checkOTP(user_otp)

            if (not res):
                print("\n<------ Invalid OTP, Please try again!! ------>\n")
                continue

            if (option == 1):
                self.userBalance()
                
            elif (option == 2):
                self.userWithdrawl()

            elif (option == 3):
                self.userDeposit()

            elif (option == 4):
                print("\n<------ THANK YOU FOR USING ATM SIMULATOR ------>\n")
                break
                
    def userBalance(self) -> str:
        print(f"\n<------ Your current balance is ₹ {self.balance} ------>\n")

    def userWithdrawl(self) -> str:
        amount = int(input("Enter the amount to withdraw: "))
        if (amount > self.balance):
            print("\n<------ Insufficient Balance !! ------>\n")
        else:
            self.balance -= amount
            print("\n<------ Amount Withdrawl Successful !! ------>\n")

    def userDeposit(self) -> str:
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print(f"\n<------ Amount Deposit ₹{amount} Successfull !! ------>\n")

    def generateOTP(self) -> str:
        self.otp = random.randrange(100000,999999)
        print(f"\n<------ Your OTP is {self.otp} ------>\n")

    def checkOTP(self,user_otp) -> bool:
        if (self.otp == user_otp):
            return True
        else:
            return False
        
if __name__ == "__main__":
    print("\n<----- WELCOME TO ATM SIMULATOR ------>\n")
    userName = input("Enter your username: ")
    passWord = input("Enter your password: ")
    user = ATM(userName,passWord)
    