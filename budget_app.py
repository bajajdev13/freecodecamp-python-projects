class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Center the name with '*' in a 30 character line
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            # Left align description up to 23 characters
            desc = f"{item['description'][:23]:<23}"
            # Right align amount up to 7 characters, 2 decimal places
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        
        total = f"Total: {self.get_balance()}"
        return title + items + total


def create_spend_chart(categories):
    spent_amounts = []
    
    # Calculate withdrawals for each category
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_amounts.append(spent)

    # Calculate percentages
    total_spent = sum(spent_amounts)
    percentages = []
    for amount in spent_amounts:
        if total_spent == 0:
            percentages.append(0)
        else:
            # Get percentage, rounded down to nearest 10
            percentages.append(int((amount / total_spent) * 10) * 10)

    # Title
    output = "Percentage spent by category\n"

    # Y-axis and bars
    for i in range(100, -1, -10):
        output += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                output += "o  "
            else:
                output += "   "
        output += "\n"

    # Horizontal dashes
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names printed vertically
    max_name_length = max(len(category.name) for category in categories)
    
    for i in range(max_name_length):
        output += "     "
        for category in categories:
            if i < len(category.name):
                output += f"{category.name[i]}  "
            else:
                output += "   "
        
        # Avoid adding a newline on the very last line
        if i < max_name_length - 1:
            output += "\n"

    return output
