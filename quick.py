def sub_sort(array,low,high):
	key=array[low]
	while low<high:
		if array[high]>=array[low]:
			high=high-1
		elif low<high:
			array[low],array[high]=array[high],array[low]
			low=low+1
	return low
def quick_sort(array,low,high):
	if low<high:
		key_index=sub_sort(array,low,high)
		quick_sort(array,low,key_index-1)
		quick_sort(array,key_index,high)
	return array

array=[2,5,1]
quick_sort(array,0,2)
for num in array:
		print(num)
