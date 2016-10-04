import sqlite3
import sys

conn = sqlite3.connect('matrix.db')

table1 = [[0 for x in range(5)]for x in range(5)]
table2 = [[0 for x in range(5)]for x in range(5)]
table3 = [[0 for x in range(5)]for x in range(5)]

cursor1 = conn.execute("SELECT row_num, col_num, value FROM A")
for row in cursor1:
	table1[row[0]][row[1]] = row[2]

cursor2 = conn.execute("SELECT row_num, col_num, value FROM B")
for row in cursor2:
	table2[row[0]][row[1]] = row[2]

for i in range(len(table1)):
	for j in range(len(table2[0])):
		for k in range(len(table2)):
	
			table3[i][j] += table1[i][k]*table2[k][j]

#print table1
#print table2
print table3

		
		

