import numpy as np

def true_damerau_levenshtein_distance(string1,string2):
	#create a list with the size of the alphabet
	da = [0] * 26
	
	length_text_1 = len(string1)
	length_text_2 = len(string2)
	
	#create d that consists a 2D array of zero with dimension length (length_text_1+2 and length_text_2+2)
	d = np.zeros((length_text_1 + 2, length_text_2 + 2))
	
	#change the last index of the d with the sum value of two string (maximum distance)
	max_distance = length_text_1 + length_text_2
	d[-1, -1] = max_distance
	
	#change the first column of the d with integer value start from 0 to the length of the first text
	for i in range(0, length_text_1 + 1):
		d[i, -1] = max_distance
		d[i, 0] = i
	
	#change the first row of the d with integer value start from 0 to the length of the first text
	for j in range(0, length_text_2 + 1):
		d[-1, j] = max_distance
		d[0, j] = j
	
	#change the d start from the second row and column until the dimension length with the minimum result of four operation (subtitution, insertion, deletion, transposition)
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
			
	#return the last value of d (the bottom left corner value before the last index of column and row that consists the maximum distance) as the smallest edit distance
	return d[length_text_1,length_text_2]
	
print(true_damerau_levenshtein_distance('an act','a cat'))
