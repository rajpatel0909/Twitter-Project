import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
A = []
B = []

def mapper(record):
    # key: document identifier
    # value: document contents
	mat = record[0]
	i = record[1]
	j = record[2]
	v = record[3]
	k = 0
	temp = []
	temp.append(mat)
	temp.append(i)
	temp.append(j)	
	temp.append(v)
	while k < 5:
		if mat == "a":
			s = str(i)+str(k)
			mr.emit_intermediate(s, temp)
			k = k + 1
		else:
			s = str(k)+str(j)
			mr.emit_intermediate(s, temp)
			k = k + 1

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
	
	result = []
	result.append(int(key[0]))
	result.append(int(key[1]))
	dic_t = {}
	dic_r = {}
	for val in list_of_values:
		if val[0] == "a":
			dic_t[str(val[2])] = val[3]
		else:
			try:
				dic_r[str(val[1])] = dic_t[str(val[1])] * val[3]
			except:
				tr = 0
				#dic_r[str(val[1])] = 0
				
	
	result.append(sum(dic_r.values()))
	#dic_r = dic_r.fromkeys(dic_r,0)
	re = (int(key[0]),int(key[1]),sum(dic_r.values()))
				
	mr.emit((re))
	#mr.emit((key, dic_r))
	'''
	mr.emit((key,list_of_values))
	'''

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)