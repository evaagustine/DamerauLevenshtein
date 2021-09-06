import numpy as np
# from itertools import product 
def true_damerau_levenshtein_distance(string1,string2):
	da = list(range(0,26))
	
	for i in range(26):
		da[(i)] = 0

	# d=np.array([for i in range(0,len(string1))]) #gayakin
	lens1 = len(string1)
	lens2 = len(string2)
	# a = np.array([i for i in range(0,lens1+2)])
	# b = np.array([i for i in range(0,lens2+1)])
	# d=np.array([a,b])
	# print(d.shape)
	# d = np.reshape(lens1+2,lens2+2)

	d ={}
	maxdistance = lens1+lens2
	d[-1,-1] = maxdistance

	for i in range(-2,lens1+2):
		d[(i,-1)] = maxdistance
		d[(i,-2)] = i+2
	
	for j in range(-2,lens2+2):
		d[(-1,j)] = maxdistance
		d[(-1,j)] = j+2
	
	for i in range(lens1):
		db=0
		for j in range(lens2):
			k=da[j]
			l=db
			if (string1[i] == string2[j]):
				cost = 0
				db = j
			else:
				cost=1
			d[(i,j)] = min(
                            d[(i-1,j-1)] + cost, # substitution
                            d[(i,j-1)] + 1, # insertion
							d[(i-1,j)] + 1, # deletion
							d[(k-1),(l-1)] + (i-k-1) + 1 + (j-l-1), #transposision
                          )
			da[i]=i
	
	return d[lens1-2,lens2-2]
	
print(true_damerau_levenshtein_distance('la i-la i', 'laki-laki'))