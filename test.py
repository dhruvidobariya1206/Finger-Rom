
import db_conn

pipquery = "Select DATE(Time), ind, mid, ring, little, thumb from angle_pip where P_id = 'C1' and Hand_Side = 'Right'"
dipquery = "Select DATE(Time), ind, mid, ring, little, thumb from angle_tip where P_id = 'C1' and Hand_Side = 'Right'"
mcpquery = "Select DATE(Time), ind, mid, ring, little, thumb from angle_mcp where P_id = 'C1' and Hand_Side = 'Right'"

db_conn.mycursor.execute(pipquery)
pip_details = db_conn.mycursor.fetchall()

db_conn.mycursor.execute(dipquery)
dip_details = db_conn.mycursor.fetchall()

db_conn.mycursor.execute(mcpquery)
mcp_details = db_conn.mycursor.fetchall()

# print(pip_details)
# for data in pip_details:
#     print(data)

# for data in pip_details:
     


