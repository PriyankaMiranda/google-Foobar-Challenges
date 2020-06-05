#Question link - https://github.com/rudisimo/google-foobar/blob/master/challenges/l2-elevator-challenge.md

#Answer-
def sort(arr_x):
	elevator = []
	for i in range(0,len(arr_x)):
		elevator_num = arr_x[i].split('.')
		elevator_num_update=[0,0,0]
		for j in range(0,len(elevator_num)):
			elevator_num_update[j]=int(elevator_num[j])
		elevator.append([elevator_num_update,len(elevator_num),arr_x[i]])

	for i in range(0,len(elevator)):
		for j in range(i+1,len(elevator)):
			swap=False	
			if (elevator[i][0][0]>elevator[j][0][0]):
				swap=True
			elif (elevator[i][0][0]==elevator[j][0][0]):

				if (elevator[i][0][1]>elevator[j][0][1]):
					swap=True
				elif(elevator[i][0][1]==elevator[j][0][1]):
					if (elevator[i][0][2]>elevator[j][0][2]):
						swap=True
			if(elevator[i][0][0]==elevator[j][0][0] and elevator[i][0][1]==elevator[j][0][1] and elevator[i][0][2]==elevator[j][0][2]):
				if(elevator[i][1]>elevator[j][1]):
					swap=True
			if (swap):
				temp=elevator[i]
				elevator[i]=elevator[j]
				elevator[j]=temp

	ans = [item[2] for item in elevator]
	return ans

if __name__ =='__main__':
	array_x = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
	answer = sort(array_x)
	print(answer)

 	