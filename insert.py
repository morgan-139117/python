
array = [1, 2, 5, 3, 6, 8, 4]


for i in range(len(array) - 2, 0, -1):
	tmp = i + 1
	for j in range(i, 0, - 1):
		#tmp = i + 1
		if (array[j] > array[tmp]):
			tmp = j

	if( tmp != i + 1):
		print tmp
		tt = array[i + 1]
		array[i + 1] = array[tmp]
		array[tmp] = tt

print array[::] 
		


