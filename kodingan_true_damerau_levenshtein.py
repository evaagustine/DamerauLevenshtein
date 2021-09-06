import numpy as np
def _is_character_same(cost, string1, string2, i, j):

	return

def true_damerau_levenshtein_distance(string1,string2):
	da = [0] * 26
	
	length_text_1 = len(string1)
	length_text_2 = len(string2)

	d = np.zeros((length_text_1 + 2, length_text_2 + 2))
	max_distance = length_text_1 + length_text_2

	d[1, 1] = max_distance

	for i in range(0, length_text_1 + 1):
		d[i, -1] = max_distance
		d[i, 0] = i
	
	for j in range(0, length_text_2 + 1):
		d[-1, j] = max_distance
		d[0, j] = j
	
	for i in range(1, length_text_1 + 1):
		db=0
		for j in range(1, length_text_2 + 1):
			k=da[j+1]
			l=db
			
			if (string1[i-1] == string2[j-1]):
				cost = 0
				db = j
			else:
				cost=1

			subtitution = d[i-1, j-1] + cost
			insertion = d[i,j-1] + 1
			deletion = d[i-1, j] + 1
			transposition = d[k-1, l-1] + (i-k-1) + 1 + (j-l-1)
			
			minimum = min(	subtitution, 
							insertion, 
							deletion, 
							transposition)

			d[i,j] = minimum
			da[i] = i
	
	print(d)
	return d[length_text_1,length_text_2]
	
print(true_damerau_levenshtein_distance('an act','a cat'))