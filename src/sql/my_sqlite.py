
class mySQLite:
  def __init__(self, userdata: UserData):
    self.userd = userdata

  def init_db(self):
    self.conn = sq3.connect("src.KalKro.db")
    self.cursor = self.conn.cursor()

    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS dialogues (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTEGER,
          user_message TEXT,
          ai_response TEXT,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
          FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    self.conn.commit()


  def show_history(self):
    self.cursor.execute("""
      SELECT user_message, ai_response, timestamp
      FROM dialogues
      WHERE user_id = (SELECT id FROM users WHERE username = ?)
      ORDER BY timestamp DESC LIMIT 10                
    """, (self.userd.username,))
    rows = self.cursor.fetchall()

    if not rows:
      printsl("\nNo dialoge history found.\n")
      return
    
    printsl("\n== Last 10 dialogues ==\n")
    for user_msg, ai_resp, ts in rows:
      printsl(f"[{ts}] You: {user_msg}")
      printsl(f"DojDo: {ai_resp}\n")

