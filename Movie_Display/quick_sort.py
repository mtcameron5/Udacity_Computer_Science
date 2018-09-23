def quickSort(a_list):
	quickSortHelper(a_list, 0, len(a_list)-1)

def quickSortHelper(a_list, first, last):
	if first < last:
		splitpoint = partition(a_list, first, last)

		quickSortHelper(a_list, first, splitpoint - 1)
		quickSortHelper(a_list, splitpoint + 1, last)

def partition(a_list, first, last):
	pivotvalue = a_list[first]

	leftmark = first + 1
	rightmark = last 

	done = False 
	while not done:

		while leftmark <= rightmark and a_list[leftmark] <= pivotvalue:
			leftmark += 1

		while a_list[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark - 1

		if rightmark < leftmark:
			done = True 
		else:
			temp = a_list[leftmark]
			a_list[leftmark] = a_list[rightmark]
			a_list[rightmark] = temp 

	temp = a_list 
	a_list[first] = a_list[rightmark]
	a_list[rightmark] = temp 

	return rightmark 


a = [5,10,13]

x = quickSort(a)
print x	