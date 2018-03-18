"""Simple bank account."""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, name, balance):
        """
        Class constructor. Each account has owner's name and starting balance.

        :param name: account owner name. String.
        :param balance: starting balance of account. Integer.
        """
        if balance < 0:
            balance = 0
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraw money from account.

        :param amount: amount to withdraw from account, has to be positive
        and the balance can't go below 0.
        """
        if amount <= 0:
            return False
        elif self.balance - amount < 0:
            return False
        else:
            self.balance = self.balance - amount
            return True

    def deposit(self, amount):
        """
        Deposit money to account.

        :param amount: amount to deposit to account, has to be positive
        """
        if amount > 0:
            self.balance += amount

    def get_balance(self):
        """
        Get account balance.

        :return: balance in double form
        """
        return self.balance

    def get_name(self):
        """
        Get account owner name.

        :return: owner name in string form
        """
        return self.name

    def transfer(self, target, amount, fee=0.01):
        """
        Transfer money where.

        :param target:
        :param amount:
        :param fee:
        :return: True if transfer happened, False otherwise
        """
        if type(target) != BankAccount:
            return False
        if amount < 0:
            return False
        if self == target:
            fee = 0
        elif self.name == target.name:
            fee *= 0.5
        total_amount = amount + (amount * fee)
        if self.balance >= total_amount:
            self.withdraw(total_amount)
            target.deposit(amount)
            return True
        else:
            return False


if __name__ == '__main__':
    mary_account = BankAccount("Mary", 100)
    guido_account = BankAccount("Guido", 150)
    mary_second_account = BankAccount("Mary", 78.01)
    assert mary_account.get_name() == "Mary"
    assert guido_account.get_name() == "Guido"
    assert mary_second_account.get_name() == "Mary"
    mary_account.deposit(10)
