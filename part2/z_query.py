import sqlite3
import sys

conn = sqlite3.connect('reuters.db')

#table1 = [[0 for x in range(5)]for x in range(5)]
#table2 = [[0 for x in range(5)]for x in range(5)]
#table3 = [[0 for x in range(5)]for x in range(5)]

cursor = conn.execute("SELECT term, count FROM frequency f1 WHERE f1.docid = '10080_txt_crude' UNION ALL SELECT term, count FROM frequency f2 WHERE f2.docid = '17035_txt_earn'")

dir0 = {}
l1 = 0
for row in cursor:
	dir0[row[0]] = l1
	l1 = l1 + 1

#print dir0
table1 = [[0 for x in range(l1)]for x in range(2)]

cursor = conn.execute("SELECT term, count FROM frequency A WHERE A.docid = '17035_txt_earn' ")

for row in cursor:
	table1[0][dir0[row[0]]] = row[1]


#print l1,
cursor = conn.execute("SELECT term, count FROM frequency A WHERE A.docid = '10080_txt_crude' ")
	
for row in cursor:
	table1[1][dir0[row[0]]] = row[1]

#print table1
#table2 = [[0 for x in range(l1)]for x in range(l1)]
#table3 = [[0 for x in range(2)]for x in range(4)]
#table3 = [[1,2],[2,1],[3,4],[1,2]]
table4 = [[0 for x in range(2)]for x in range(2)]
i = 0
while i<2:
	j = i
	while j < 2:
		k = 0
		while k < l1:
			table4[i][j] += table1[i][k]*table1[j][k]
			k += 1
		table4[j][i] = table4[i][j]
		j += 1
	i += 1

#print table4
a = table4[0][0]+table4[0][1]  
b = table4[1][0]+table4[1][1]
print "10080_txt_crude|",a
print "17035_txt_earn|",b

		
		

