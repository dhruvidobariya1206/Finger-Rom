import sqlite3

mydb = sqlite3.connect("datafile.db")

mycursor=mydb.cursor()

mycursor.execute('''CREATE TABLE IF NOT EXISTS angle_mcp (
  SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
  P_id TEXT NOT NULL,
  Hand_Side TEXT NOT NULL,
  Time DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ind REAL,
  mid REAL,
  ring REAL,
  little REAL,
  thumb REAL
);''')

mycursor.execute('''CREATE TABLE IF NOT EXISTS angle_pip (
  SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
  P_id TEXT,
  Hand_Side TEXT NOT NULL,
  Time DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ind REAL NOT NULL,
  mid REAL NOT NULL,
  ring REAL NOT NULL,
  little REAL NOT NULL,
  thumb REAL
);''')

mycursor.execute('''CREATE TABLE IF NOT EXISTS angle_tip (
  SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
  P_id TEXT NOT NULL,
  Hand_Side TEXT NOT NULL,
  Time DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ind REAL,
  mid REAL,
  ring REAL,
  little REAL,
  thumb REAL
);''')

mycursor.execute('''CREATE TABLE IF NOT EXISTS patients (
  Patient_ID TEXT,
  First_Name TEXT,
  Middle_Name TEXT NOT NULL,
  Last_Name TEXT NOT NULL,
  PPhone TEXT UNIQUE,
  Gender TEXT DEFAULT 'M',
  Age INTEGER NOT NULL DEFAULT 0,
  Occupation TEXT NOT NULL,
  UNIQUE (Patient_ID)
);''')