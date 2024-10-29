import sqlite3

class DB:
  def __init__(self, connUrl: str):
    self.url = connUrl
    self._initiate_connection()
    
  def _initiate_connection(self):
    self.conn = sqlite3.connect(self.url)
    self.cursor = self.conn.cursor()
  
  def add_expense(self, expense: str, value: float):
    self.cursor.execute("INSERT INTO expenses(name, value) VALUES(?, ?)", (expense, value))
    print("Expense added: ", expense, value)
    self.conn.commit()
    return (expense, value)
  
  def get_all_expenses(self):
    data = []
    for row in self.cursor.execute("SELECT * FROM expenses"):
      data.append(row)
    return data
    

class ExpenseUnit:
  def __init__(self, id: int, name: str, value: float):
    self.id = id
    self.name = name
    self.value = value