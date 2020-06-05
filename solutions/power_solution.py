#Question link - https://github.com/rudisimo/google-foobar/blob/master/challenges/l2-power-hungry.md

#Answer-

def separate_arrs(arr_x):
	pos_arr = []
	neg_arr = []
	for elem in arr_x:
		if elem > 0:
			pos_arr.append(elem)
		elif elem < 0:
			neg_arr.append(elem)
	return pos_arr, neg_arr

def get_product(arr_x):
	product = 1
	for elems in arr_x:
		product = product * elems
	return product

def remove_smallest_elem(arr_x):
	# we remove the smallest negative value 
	# hence we actually find the maximum value
	min_val = arr_x[0]
	min_val_loc = 0
	for i in range(1,len(arr_x)):
		if(arr_x[i]>min_val):
			min_val = arr_x[i]
			min_val_loc = i
	
	for i in range(min_val_loc, len(arr_x)-1):
		arr_x[i] = arr_x[i+1]  
	arr_x.pop()
	return arr_x

if __name__ =='__main__':
	inputs = [-2, -3, 4, -5]

	if(len(inputs) > 0):
		output = separate_arrs(inputs)
		pos_array_len = len(output[0])
		neg_array_len = len(output[1])
		if(pos_array_len > 0):
			# if there are positive or negative values 
			pos_product = get_product(output[0])
			# positive product is the highest possible product so far 
			if(neg_array_len > 1):
				neg_arr = output[1]
				if(neg_array_len%2 != 0):
					neg_arr = remove_smallest_elem(output[1])
				neg_product = get_product(neg_arr)
			else:
				neg_product = 1
			max_product = pos_product * neg_product
		else:
			# if there are no positive or negative values
			# but the original array has length > 0 
			# that means they are all zeros 
			max_product = 0 

		print("Max product: "+str(max_product))
	else:
		print("Empty array!!")

	# inputs = order_array(inputs)
	# reverse_inputs = get_reverse_array(inputs)
	# get_max_power(inputs,reverse_inputs)


	