

#Question link - https://github.com/rudisimo/google-foobar/blob/master/challenges/l1-prison-labor-dodgers.md

#Answer-

def get_elem():
	x = [14, 27, 1, 4, 2, 50, 3, 1]
	y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
	x1=0
	y1 = 0
	for i in range(0,len(x)):
		x1=x1+x[i]
	for i in range(0,len(y)):
		y1=y1+y[i]
	return ((x1-y1) if(len(x)>len(y)) else (y1-x1))

if __name__ =='__main__':
	answer = get_elem()
	print(answer)

