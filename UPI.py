# pin_choice,balance_choice,pay_amount,ballance,default_pin,q,x,input_pin,y
def pay():
    def transection():
        ballance=ammount
        mobile_no=int(input("pay to Number : "))
        pay_amount=int(input("Enter you ammount to pay : "))
        if pay_amount<=ballance:
            x=0
            while (x!=3):          #loop for Giving Chance For Correct pin
                x=x+1
                pin=int(input("Enter your pin "))
                if pin==default_pin: 
                    print("Processing Transection")
                    print("your payment of ",pay_amount," is succesfull to ",mobile_no)
                    print("Your current balance is : ",ballance-pay_amount)
                    break    # Function Ends
                else:
                    print("WaRNING : Wrong Pin\n        Payment failed")
                    print("        Try Again")
            else:
                print("Too many attempt")
                print("Card blocked")
        else:
            print("invalid ballance (try again)")
    ammount=100000
    print("your current Balance is : ",ammount,"\n")
    print("optin :\n")
    print("1. Add Money")
    print("2. Continue\n")
    balance_choice=int(input(print("chose One\n")))
    if balance_choice==1:
        pay_amount=int(input("Enter the ammount you want to add "))
        y=0             #loop for ammount update
        while (y!=3):
            y=y+1
            input_pin=int(input(print("Enter your pin")))
            print("\n Updated Balance : ",ammount+pay_amount)
            if input_pin==default_pin:
                ammount+=pay_amount
                transection()
                break
            else:
                print("Wrong Pin")
        else:
            print("Wrong Pin")
    else:
        transection()
    print("THaNK YOU FOR SHOWING YOUR INTREST ")
# Main function start from here
input(print("Enter your Card Number"))        #user data required in Further update
input(print("Enter your card cvv"))
print("Default pin = 0\n")
print("option\n")
print("1.Change Pin")
print("2. Continue\n")
pin_choice=int(input(print("Chose One")))
if pin_choice==1:
    Tpin=int(input(print("\nEnter New pin")))
    Mpin=int(input(print("Confirm Pin")))
    default_pin=Tpin
    if Tpin==Mpin:
        print("\nYour New pin set up is Succesfull")
        print("New pin : ",Tpin)
        print("")
        pay()
    else:
        print("pin doesn't match")
elif pin_choice==2:
    default_pin=0
    pay()
else:
    print("Invalid Choice")