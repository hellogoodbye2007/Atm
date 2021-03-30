class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50000.")
    
    def cash_withdrawal(self, amount):
        new_amount = 50000 - amount
        print(f"You have withdrawn amount {amount}. Your remaining balance is {new_amount}.")

def main():
    cardnumber = input("Insert your card number: ")
    pinnumber = input("Insert your pin number: ")

    newuser = Atm(cardnumber, pinnumber)

    print("Choose your activity")
    print("1. Balance Inquiry 2.Withdraw Cash")
    activity = int(input("Enter activity number, 1 or 2: "))
    if(activity == 1):
        newuser.check_balance()
    elif(activity == 2):
        amount = int(input("Enter the amount to withdraw: "))
        newuser.cash_withdrawal(amount)
    else:
        print("Enter a valid number")

main()