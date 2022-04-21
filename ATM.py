class ATM:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your Balance Is 500000")

    def withdrawal(self,amount):
        #amount = input("Enter The Amount To Be Withdrawn")
        new_balance = 500000-amount
        print("You have widthdrawn "+ str(amount)+"you remaining balance is"+ str(new_balance))

def main():
    card_number = input("Enter Your Card Number")
    pin_number = input("Enter Your PIN Number")
    aa = ATM(card_number, pin_number)
    activity=int(input("Enter activity number"))
    if(activity==1):
        aa.check_balance()
    elif(activity==2):
        amount=int(input("Enterthe Amount"))
        aa.withdrawal(amount)
    else:
        print("EnterA valid Number")
    #print(aa.withdrawal(2222))

if __name__=="__main__":
    main()