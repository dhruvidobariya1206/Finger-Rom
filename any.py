import db_conn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

query1 = "Select ind, mid, ring, little, thumb from angle_pip where P_id='1' ORDER BY SrNo DESC LIMIT 2;"
# print(query1)
db_conn.mycursor.execute(query1)
row1 = db_conn.mycursor.fetchall()

query2 = "Select ind, mid, ring, little, thumb from angle_tip where P_id='1' ORDER BY SrNo DESC LIMIT 2;"
# print(query1)
db_conn.mycursor.execute(query2)
row2 = db_conn.mycursor.fetchall()

query2 = "Select ind, mid, ring, little, thumb from angle_mcp where P_id='1' ORDER BY SrNo DESC LIMIT 2;"
# print(query1)
db_conn.mycursor.execute(query2)
row3 = db_conn.mycursor.fetchall()

# fib,ax=plt.subplots()
prev_pip=np.array(row1[1])
curr_pip=np.array(row1[0])
prev_tip=np.array(row2[1])
curr_tip=np.array(row2[0])
prev_mcp=np.array(row3[1])
curr_mcp=np.array(row3[0])
# # df = pd.dataframe

# max= np.maximum(prev, curr) 
# max_val=0
# for i in range(len(max)):
#     if(max[i]>max_val):
#         max_val=max[i]

# print(prev)
# print(curr)
x=['index','middle','ring','little','thumb']
plt.plot(x,prev_pip,label="Prev PIP", marker="o", linestyle = 'dashed',c = '#4CAF50')
plt.plot(x,curr_pip, label="curr PIP", marker="o",c = '#4CAF50')
plt.plot(x,prev_tip,label="Prev TIP", marker="o", linestyle = 'dashed',c = '#AAAF50')
plt.plot(x,curr_tip, label="curr TIP", marker="o",c = '#AAAF50')
plt.plot(x,prev_mcp,label="Prev MCP", marker="o", linestyle = 'dashed',c = '#4CAFAA')
plt.plot(x,curr_mcp, label="curr MCP", marker="o",c = '#4CAFAA')
plt.xlabel("Finger")
plt.ylabel("Angle Measure")
plt.title('Progress')
plt.legend(loc='upper right')
plt.show()


# # annotation = ax.annotate(
# #     text='',
# #     xy=(0,0),
# #     xytext=(15,15),
# #     textcoords="offset points",
# #     bbox={'boxstyle':'round','fc':'w'},
# #     # arrowprops={'arrowstyle':}
# # )
# # annotation.set_visible(False)


# # fig = px.line(x,prev, x="finger", y="angle")
# # fig.update_traces(mode="markers+lines")
# # fig.show()




# plt.annotate("hey",xy=(0,0), xytext=(10,10), bbox={'boxstyle': 'round', 'fc': 'w'}, arrowprops={'arrowstyle': '->'})
# annotation.set_visible(False)






# fig, geeeks = plt.subplots()
  
# t = np.arange(0.0, 5.0, 0.001)
# s = np.cos(3 * np.pi * t)
# line = geeeks.plot(prev, s, lw = 2)
  
# # Annotation
# geeeks.annotate('Local Max', xy =(3.3, 1),
#                 xytext =(3, 1.8), 
#                 arrowprops = {'arrowstyle': '->'})
  
# geeeks.set_ylim(-2, 2)
  
# Plot the Annotation in the graph
# plt.show()