import mysql.connector as msc


# host = "localhost"              # ip on which the db server is hosted
# port = "8080"                   # port on which the db is hosted
# user = "root"                  # username to access db server
# password = ""          # password to access db server
# db = "hcd"             # name of the database to access



mydb = msc.connect(host="sql107.epizy.com", port="3306", user="epiz_33843643", password="Kana120602", database="hcd")        # establishing a connection with the database server
mycursor = mydb.cursor(buffered=True)            # accessing the cursor of the database



# query = "Select * from patients"          # define the query as a string e.g. select * from

# mycursor.execute(query)             # executing a query on the database
mydb.commit()                       # commit after making changes to the db