#Question link - https://github.com/rudisimo/google-foobar/blob/master/challenges/l2-ion-flux-relabeling.md

#Answer-

def generate_tree(h):
	i=0
	nodes=2**(h)-1
	height=0
	combined_tree=[]
	i=1
	while(i<=nodes):
		if (len(tree)>=2 and tree[len(tree)-1][2] == tree[len(tree)-2][2]):#if two nodes have parent as null
			a=tree.pop()
			b=tree.pop()
			parent_height=a[2]+1
			a[1]=i
			b[1]=i
			tree.append([i,'null',parent_height])
			i=i+1	
			combined_tree.append(a)
			combined_tree.append(b)
		else:
			tree.append([i,'null',height])

			i=i+1
	c=tree.pop()
	c[1]=-1
	combined_tree.append(c)
	return combined_tree

def check_locs(list_x,tree_x):
	locations=[]
	for elem in list_x:
		for node in tree_x:
			if (elem == node[0]):
				locations.append(node[1])
	return locations 

if __name__ =='__main__':
	h = 5
	q = [7, 3, 5, 1]
	tree=[]	
	combined_tree = generate_tree(h)
	locs = check_locs(q,combined_tree)
	print(locs)