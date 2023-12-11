import winsound
class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        self.balance = 5000  # Initial balance set to 5000
        self.locked = False  # Account lock status
        self.failed_login_attempts = 0

    def deposit(self, amount, denominations):
        if self.locked:
            return "Account is locked."
        
        total_deposited = sum(amount * denomination for amount, denomination in zip(amount, denominations))
        if total_deposited <= 100000:  # Maximum deposit limit 1L
            self.balance += total_deposited
            return "Deposit successful."
        else:
            return "Deposit limit exceeded."

    def withdraw(self, amount, denominations):
        if self.locked:
            return "Account is locked."
        
        total_withdrawn = sum(amount * denomination for amount, denomination in zip(amount, denominations))
        if total_withdrawn <= 50000:  # Maximum withdrawal limit 50k
            if total_withdrawn <= self.balance:
                self.balance -= total_withdrawn
                return "Withdrawal successful."
            else:
                return "Insufficient balance."
        else:
            return "Withdrawal limit exceeded."

    def check_balance(self):
        if self.locked:
            return "Account is locked."
        return f"Balance: {self.balance}"

    def change_password(self, current_password, new_password):
        if self.locked:
            return "Account is locked."
        if self.password == current_password:
            self.password = new_password
            return "Password changed successfully."
        else:
            return "Incorrect current password."

    def login(self, user_id, password):
        if not self.locked:
            if user_id == self.user_id and password == self.password:
                self.failed_login_attempts = 0
                return "Login successful."
            else:
                self.failed_login_attempts += 1
                if self.failed_login_attempts >= 3:
                    self.locked = True
                    return "Account locked due to multiple failed login attempts."
                else:
                    return "Incorrect user ID or password. Please try again."
        else:
            return "Account is locked."


class Admin:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        self.total_balance = 300000  # Maximum balance up to 3L
        self.denominations = [100, 200, 500, 2000]  # Available denominations
        self.notification_threshold = 75000  # Balance notification threshold

    def get_total_balance(self):
        return f"Total balance: {self.total_balance}"

    def deposit_cash(self, amount, denominations):
        total_deposited = sum(amount * denomination for amount, denomination in zip(amount, denominations))
        if total_deposited <= 300000:  # Maximum cash deposit 3L
            self.total_balance += total_deposited
            return "Cash deposit successful."
        else:
            return "Cash deposit limit exceeded."

    def notify_low_balance(self):
        if self.total_balance < self.notification_threshold:
            return "Low balance notification: Please consider adding funds."

# Example usage:
user1 = User("user1", "password1")
admin = Admin("admin", "adminpass")

# User actions
print(user1.login("user1", "password1"))
print(user1.deposit([2, 5], [500, 2000]))
print(user1.withdraw([2, 5], [500, 2000]))
print(user1.check_balance())
print(user1.change_password("password1", "newpass"))

# Admin actions
print(admin.get_total_balance())
print(admin.deposit_cash([2, 5], [500, 2000]))
print(admin.notify_low_balance())
