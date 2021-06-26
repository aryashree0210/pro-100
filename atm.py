class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def Balance(self):
        print("Your balance is 40000")

    def withdrawl(self,amount):
        new_amount = 40000 - amount
        print("Money withdrawn " ) 


def main():
    Card_number = input("enter card number: ")
    pin_number  = input("enter  pin number:")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose any one activity  ")
    print("1. Balance amount  2. withdrawl")
    activity = int(input("enter the amount : "))

    if (activity == 1):
        new_user.Balance()
    elif (activity == 2):
        amount = int(input("enter the amount: "))
        new_user.withdrawl(amount)
    else:
        print("enter the amount")


if __name__ == "__main__":
    main()


    