class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        if amount <= 0:
            return False
        self.ledger.append({'amount': amount, 'description': description})
        return True
        #please only use Natural Numbers

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    #Total expense
    def get_total_spent(self):
        total = 0
        for item in self.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        return total
        
    #count of withdraw
    def get_transaction_count(self):
        return len(self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        output = self.name.center(30, '*') + "\n"
        for item in self.ledger:
            description = item['description'][:23]
            amount = item['amount']
            output += f"{description:<23}{amount:>7.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

"""function for total withdrawals, percentage of total spending"""
def create_spend_chart(categories):
    spent = []
    for category in categories:
        spent.append(category.get_total_spent())

    total_spent = sum(spent)

    percentages = []
    for amount in spent:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int(amount / total_spent * 10) * 10)

    """I would have like to use matplotlib library here but it was not mention in the certification course"""
    # 3. title and bars
    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for percent in percentages:
            chart += " o " if percent >= level else "   "
        chart += " \n"

    # 4. horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1)

    # 5. vertical names
    longest = max(len(category.name) for category in categories)
    for i in range(longest):
        chart += "\n     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

    return chart