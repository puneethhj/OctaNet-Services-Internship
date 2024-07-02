class Account:
    def __init__(self, initial_balance, initial_pin):
        self.balance = initial_balance
        self.pin = initial_pin
        self.transactions = []

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: ${amount}")
            return f"${amount} withdrawn successfully"

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        return f"${amount} deposited successfully"

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            self.transactions.append("PIN changed successfully")
            return "PIN changed successfully"
        else:
            return "Incorrect old PIN"

    def get_transaction_history(self):
        return self.transactions


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, initial_balance, initial_pin):
        if account_id in self.accounts:
            return "Account already exists"
        else:
            self.accounts[account_id] = Account(initial_balance, initial_pin)
            return "Account created successfully"

    def balance_inquiry(self, account_id, pin):
        if account_id in self.accounts:
            account = self.accounts[account_id]
            if account.pin == pin:
                return account.check_balance()
            else:
                return "Incorrect PIN"
        else:
            return "Account not found"

    def withdraw_cash(self, account_id, pin, amount):
        if account_id in self.accounts:
            account = self.accounts[account_id]
            if account.pin == pin:
                return account.withdraw(amount)
            else:
                return "Incorrect PIN"
        else:
            return "Account not found"

    def deposit_cash(self, account_id, amount):
        if account_id in self.accounts:
            account = self.accounts[account_id]
            return account.deposit(amount)
        else:
            return "Account not found"

    def change_pin(self, account_id, old_pin, new_pin):
        if account_id in self.accounts:
            account = self.accounts[account_id]
            return account.change_pin(old_pin, new_pin)
        else:
            return "Account not found"

    def transaction_history(self, account_id, pin):
        if account_id in self.accounts:
            account = self.accounts[account_id]
            if account.pin == pin:
                return account.get_transaction_history()
            else:
                return "Incorrect PIN"
        else:
            return "Account not found"


# Example usage:
# Create an ATM instance
atm = ATM()

# Create an account
print(atm.create_account("123456", 1000, 1234))  # Account created successfully

# Deposit money
print(atm.deposit_cash("123456", 500))  # $500 deposited successfully

# Withdraw money
print(atm.withdraw_cash("123456", 1234, 200))  # $200 withdrawn successfully

# Check balance
print(atm.balance_inquiry("123456", 1234))  # 1300

# Change PIN
print(atm.change_pin("123456", 1234, 5678))  # PIN changed successfully

# Check transaction history
print(atm.transaction_history("123456", 5678))
# ['Deposit: $500', 'Withdraw: $200', 'PIN changed successfully']
