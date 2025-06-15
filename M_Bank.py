class UPIApp:  
    def __init__(self):  
        self.balance = 1000  # Initial balance for demonstration  
        self.transaction_history = []  

    def display_balance(self):  
        print(f"Current Balance: ₹{self.balance}")  

    def make_payment(self, amount, upi_id):  
        if amount <= 0:  
            print("Invalid amount. Please enter a positive value.")  
            return  
        if amount > self.balance:  
            print("Insufficient balance.")  
            return  
        
        # Simulate payment processing  
        print(f"Processing payment of ₹{amount} to {upi_id}...")  
        self.balance -= amount  
        self.transaction_history.append((upi_id, amount))  
        print("Payment successful!")  
        self.display_balance()  

    def view_transaction_history(self):  
        if not self.transaction_history:  
            print("No transactions found.")  
            return  
        print("Transaction History:")  
        for upi_id, amount in self.transaction_history:  
            print(f"Paid ₹{amount} to {upi_id}")  

def main():  
    app = UPIApp()  
    app.display_balance()  

    while True:  
        print("\nOptions:")  
        print("1. Make Payment")  
        print("2. View Transaction History")  
        print("3. Exit")  
        choice = input("Choose an option: ")  

        if choice == '1':  
            try:  
                amount = float(input("Enter amount to pay: "))  
                upi_id = input("Enter UPI ID: ")  
                app.make_payment(amount, upi_id)  
            except ValueError:  
                print("Invalid input. Please enter a numeric value for the amount.")  
        elif choice == '2':  
            app.view_transaction_history()  
        elif choice == '3':  
            print("Exiting the app.")  
            break  
        else:  
            print("Invalid choice. Please select a valid option.")  

if __name__ == "__main__":  
    main()