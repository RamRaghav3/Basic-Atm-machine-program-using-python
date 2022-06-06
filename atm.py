


class ATM: 
    a = "WELCOME! STATE BANK OF INDIA ATM!"
    print(a)
    def machine(self,name):
        Balance = 10000
        self.name = name
        b = int(input("Enter your Pin : "))
        if (b == 2001):
            c = int(input(f"Welcome! {self.name}\nPress 1 for To check Balance\nPress 2 for Deposting\nPress 3 for WithDrawal\n"))
            if (c == 1):
                f = input("enter your Name : ")
                h = int(input("enter your Account Number : "))
                if(f == "Raghava" and h== 203310452):
                    print(f'Your Balance : {Balance}')
                    exit()
                else :
                    print("Wrong Details Try Again")
                    exit()
            if(c == 2):
                added_balance = int(input("enter the amount to be deposited : "))
                Balance = added_balance + Balance
                print("Your amount has been successfully deposited in our Bank! Thank you")
                print(f"Your balance after deposited is : {Balance}")
                exit()
            if (c == 3):
                withdrawl = int(input("Enter the amount to be withdrawed : "))
                Balance = Balance - withdrawl
                print(f"Collect the Cash {Balance} Thankyou! Visit again...")
            else :
                print("You Have pressed the wrong Digit PLz try Again...")

            


        else :
            print("wrong pin try again")
obj = ATM()
obj.machine("Raghav")

        