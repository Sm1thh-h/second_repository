import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.expense_id = str(uuid.uuid4()) # unique identifier
        self.title = title # title of the expense
        self.amount = amount #amount of the expense
        self.created_at = datetime.now(timezone.utc) # When it was created
        self.updated_at = None #initially same as created_at

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc) # update the timestamp when the expense is updated

    def to_dict(self): # convert object to a dictionary representation
        return{
            "id":self.expense_id,
            "title":self.title,
            "amount":self.amount,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
    



class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.expense_id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

    


# Demonstration
# Create an instance of ExpenseDB
expense_db = ExpenseDB()

# Add a few expenses
expense1 = Expense("Groceries", 50.75)
expense2 = Expense("Rent", 1200)
expense3 = Expense("Internet", 60)

expense_db.add_expense(expense1)
expense_db.add_expense(expense2)
expense_db.add_expense(expense3)


# Convert expenses to dictionary format
expenses_dict = expense_db.to_dict()

# Retrieve an expense by ID
retrieved_expense = expense_db.get_expense_by_id(expense1.expense_id)

# Retrieve expenses by title
retrieved_expenses_by_title = expense_db.get_expense_by_title("Internet")


# Output results
retrieved_expense_data = retrieved_expense.to_dict() if retrieved_expense else None
retrieved_expenses_by_title_data = [exp.to_dict() for exp in retrieved_expenses_by_title]

print(expenses_dict, retrieved_expense_data, retrieved_expenses_by_title_data)