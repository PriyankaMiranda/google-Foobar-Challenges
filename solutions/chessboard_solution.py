
#Question link - https://github.com/rudisimo/google-foobar/blob/master/challenges/l2-dont-get-volunteered.md

#Answer-

def start():
	src = 0
	queue.append([src,'null',level])
	actions_arr = get_actions()

def get_loc(val):
	orig_y=val//8
	orig_x=val-8*orig_y
	moves=[val-17,val-15,val-10,val-6,val+6,val+10,val+15,val+17]
	possible_moves=[]
	for i in range(0,len(moves)):
		y=moves[i]//8
		x=moves[i]-8*y
		if(orig_x-x>2 or x-orig_x>2 or orig_y-y>2 or y-orig_y>2 or moves[i]<0 or moves[i]>63):
			continue
		else:
			possible_moves.append(moves[i])	
	return possible_moves

def get_actions():
	check=queue.pop(0)
	level = check[2] + 1
	visited[check[0]]=True;
	
	if(check[0]==dest):
		print(check)
		get_parent(check)
		print('Path:'+history)
		print('Length of path:'+len(history-1))
	else:
		children = get_loc(check[0])
		for child in children:
			if(visited[child]):
				continue
			queue.append([child,check,level])
		get_actions()

def get_parent(child):
	history.append(child[0])
	if (child[1] == 'null' ):
		return history
	else:
		return get_parent(child[1])


if __name__ =='__main__':
	history=[]
	level=0
	queue = []
	dest = 63
	visited = [False] * (64) 
	path = start()
