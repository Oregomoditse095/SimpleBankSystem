# SimpleBankSystem
---
# Bank Account Management System

This Python project provides a simple bank account management system with support for clients, staff members, and business accounts. It demonstrates object-oriented programming (OOP) concepts and includes the following classes:

1. **Client**: Represents information about a bank account holder.
2. **Staff**: Stores details about staff members (e.g., managers, tellers).
3. **BankAccount**: A base class for managing individual accounts.
4. **BusinessAccount**: Inherits from `BankAccount` and adds business-specific features.

## Usage

1. **Client Information**:
   - Create a `Client` object by providing the client's name, address, and phone number.
   - Associate the client information with a bank account using the `set_client_info` method.

2. **Staff Details**:
   - Create a `Staff` object with a staff ID, name, and position.
   - Staff members can be managers, tellers, or other roles.

3. **Bank Account Operations**:
   - Create a `BankAccount` or `BusinessAccount` object.
   - Deposit funds using the `deposit` method.
   - Withdraw funds using the `withdraw` method.
   - Check the account balance using the `get_balance` method.

4. **Business Accounts**:
   - Use the `BusinessAccount` class for business clients.
   - Add benefits specific to business accounts using the `add_benefit` method.
   - Retrieve the list of benefits using the `get_benefits` method.

## Example

```
from bank_system import Client, Staff, BusinessAccount

# Create a client
alice_info = Client(name="Alice Johnson", address="123 Main St, Anytown", phone_number="555-123-4567")

# Create a staff member
staff_member = Staff(staff_id=101, name="John Doe", position="Manager")

# Create a business account
my_account = BusinessAccount(account_holder="Alice", initial_balance=1000, business_name="ABC Corp")
my_account.set_client_info(alice_info)
my_account.deposit(500)
my_account.withdraw(200)
my_account.add_benefit("Free business consultations")
my_account.add_benefit("Higher transaction limits")

# Display account details
print(f"Current balance for {my_account.account_holder}: ${my_account.get_balance()}")
print(f"Client info: {my_account.client_info.name}, {my_account.client_info.address}, {my_account.client_info.phone_number}")
print(f"Business benefits: {', '.join(my_account.get_benefits())}")
print(f"Staff member: {staff_member.name}, ID: {staff_member.staff_id}, Position: {staff_member.position}")
```
