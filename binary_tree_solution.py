
def generate_tree(h):
	i=0
	nodes=2**(h)-1
	height=0
	combined_tree=[]
	i=1
	while(i<=nodes):
		if (len(tree)>=2 and tree[len(tree)-1][2] == tree[len(tree)-2][2]):#if two nodes have parent as null
			#find elems with same order
			a=tree.pop()
			b=tree.pop()
			parent_height=a[2]+1
			a[1]=i
			b[1]=i
			tree.append([i,'null',parent_height])
			i=i+1	
			combined_tree.append(a)
			combined_tree.append(b)
			#create parent for both
		else:
			tree.append([i,'null',height])

			i=i+1

			#otherwise, create a new node with an empty parent null 
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

def print_tree(tree_x):
	print(tree_x)
	i=len(tree_x)-1
	order=2
	while(order>=0):
		try:
			while(tree_x[len(tree_x)-1][2] == order):
				print(tree_x.pop(),end =" ")
		except:
			print('')
		order=order-1

	
if __name__ =='__main__':
	h = 50
	q = [7, 3, 5, 1]
	tree=[]	
	combined_tree = generate_tree(h)
	# print_tree(combined_tree)
	locs = check_locs(q,combined_tree)
	print(locs)