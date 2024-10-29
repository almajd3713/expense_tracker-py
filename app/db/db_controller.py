import sqlite3

class DB:
  def __init__(self, connUrl: str):
    self.url = connUrl
    
  def _initiate_connection(self):
    self.conn = sqlite3.connect(self.url)
    self.cursor = self.conn.cursor()
  
  def add_expense(self, expense: str, value: float):
    self.cursor.execute("INSERT INTO EXPENSE VALUES(?, ?)", (expense, value))
    print("Expense added: ", expense, value)
  
  def get_all_expenses(self):
    data = []
    for row in self.cursor.execute("SELECT * FROM EXPERNSES"):
      data.append(row)
    return data
    

class ExpenseUnit:
  def __init__(self, name: str, value: float):
    self.name = name
    self.value = value