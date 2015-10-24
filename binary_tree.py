class Binary_Tree(object):
	"""my name is Binary_Tree , i have one head and two arms B| """
	def __init__(self, node):
		self.node = node
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None 

    def set_left_branch(self, node):
        self.leftBranch = node

    def set_right_branch(self, node):
        self.rightBranch = node

    def set_parent(self, parent):
        self.parent = parent

    def get_value(self):
        return self.value

    def get_left_branch(self):
        return self.leftBranch

    def get_right_branch(self):
        return self.rightBranch

    def get_parent(self):
        return self.parent

    def __str__(self):
        return self.value 
	
	def depth_first_search(root_node, function):
		''' go deep or fall asleep B| '''
		nodes_stack = []
		while len(nodes_stack) > 0 : 
			print "we are at node" + str (nodes_stack[0].get_value())

			if function (nodes_stack[0]):
				print "we found it !"
				return True
			else :
				current_node = nodes_stack.pop()
				if current_node.get_right_branch():
					nodes_stack.insert(0, current_node.get_right_branch())

				if current_node.get_left_branch():
					nodes_stack.insert(0, current_node.get_left_branch())
		print " we didn't find it , you should know that it  isn't my fault , but  it yours :/ "
		return False

	def bredth_first_search(root_node, function):
		'''search well or go to hell :3 '''
		nodes_queue = []
		while len(nodes_queue) > 0:
			print " we are at the node " + str(nodes_queue[0].get_value())
			if function(nodes_queue[0]) : 
				print "finally we found it B|"
				return True 
			else :
				current_node = nodes_queue.pop()

				if current_node.get_right_branch():
					nodes_queue.append(current_node.get_right_branch())

				if current_node.get_left_branch():
					nodes_queue.append(current_node.get_right_branch())
		print " we didn't find it , you should know that it  isn't my fault , but  it yours :/ "
		return False