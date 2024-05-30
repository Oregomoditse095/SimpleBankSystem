class Client:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number


class Staff:
    def __init__(self, staff_id, name, position):
        self.staff_id = staff_id
        self.name = name
        self.position = position


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.client_info = None  # Initialize client info as None

    def set_client_info(self, client):
        """Set the client information."""
        self.client_info = client

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        """Get the current account balance."""
        return self.balance


class BusinessAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0, business_name=""):
        super().__init__(account_holder, initial_balance)
        self.business_name = business_name
        self.benefits = []  # Initialize benefits as an empty list

    def add_benefit(self, benefit):
        """Add a benefit to the business account."""
        self.benefits.append(benefit)

    def get_benefits(self):
        """Get the list of benefits for the business account."""
        return self.benefits


# Example usage:
if __name__ == "__main__":
    alice_info = Client(name="Alice Johnson", address="123 Main St, Anytown", phone_number="555-123-4567")
    staff_member = Staff(staff_id=101, name="John Doe", position="Manager")

    my_account = BusinessAccount(account_holder="Alice", initial_balance=1000, business_name="ABC Corp")
    my_account.set_client_info(alice_info)
    my_account.deposit(500)
    my_account.withdraw(200)
    my_account.add_benefit("Free business consultations")
    my_account.add_benefit("Higher transaction limits")

    print(f"Current balance for {my_account.account_holder}: ${my_account.get_balance()}")
    print(
        f"Client info: {my_account.client_info.name}, {my_account.client_info.address}, {my_account.client_info.phone_number}")
    print(f"Business benefits: {', '.join(my_account.get_benefits())}")
    print(f"Staff member: {staff_member.name}, ID: {staff_member.staff_id}, Position: {staff_member.position}")
