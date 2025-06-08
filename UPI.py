# a,b,c,d,p,q,x,e,y
def pay():
    def transection():
        d=ammount
        No=int(input("pay to Number : "))
        c=int(input("Enter you ammount to pay : "))
        if c<=d:
            x=0
            while (x!=3):          #loop for Giving Chance For Correct pin
                x=x+1
                pin=int(input("Enter your pin "))
                if pin==p: 
                    print("Processing Transection")
                    print("your payment of ",c," is succesfull to ",No)
                    print("Your current balance is : ",d-c)
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
    b=int(input(print("chose One\n")))
    if b==1:
        c=int(input("Enter the ammount you want to add "))
        y=0
        while (y!=3):
            y=y+1
            e=int(input(print("Enter your pin")))
            print("\n Updated Balance : ",ammount+c)
            if e==p:
                ammount+=c
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
input(print("Enter your Card Number"))        #use if update Further
input(print("Enter your card cvv"))
print("Default pin = 0\n")
print("option\n")
print("1.Change Pin")
print("2. Continue\n")
a=int(input(print("Chose One")))
if a==1:
    Tpin=int(input(print("\nEnter New pin")))
    Mpin=int(input(print("Confirm Pin")))
    p=Tpin
    if Tpin==Mpin:
        print("\nYour New pin set up is Succesfull")
        print("New pin : ",Tpin)
        print("")
        pay()
    else:
        print("pin doesn't match")
elif a==2:
    p=0
    pay()
else:
    print("Invalid Choice")