# What is a link list?
# A collection of nodes, where each node has two attributes, data it holds and the pointer to the next node
# What is a node?
# A container for some sort of data

# the constructor for a class in py is __init__

"""
Disadvantage
    - slow to get to the xth element
        - o(n) -> linear

Advantage
    - insert and delete can be quick
        - o(1) prepend
        - o(n) append
    
"""

# Node class:
class Node():
    # Constructor/initilization:
    # pointer is of default None, so when at the end of the list it points no where
    def __init__(self, data, pointer = None):
        self.data = data
        self.pointer = pointer



class Linklist:
    # init is a constructor that instatiates an object and sets instance attributes.
    def __init__(self, head_node):
        # head node is an instance attribute.
        # instance attribute: Per instance this attribute is different
        self.head_node = head_node


    def search(self, data):
        """
        Search wants to see if a value lives anywhere inside of a link list
        Inside of all the nodes do you have one node, or any amount of node - that contain this data I'm sending you


        parameters:
            some sort of data type
                string, number, whatever you give it. Just not a node

        return value:
            either a node or False
            easier: return True or False


        (head, my data- yes or no) -> (data: yes or no) ->....->(tail: yes or no; return false)
        """
        current_node = self.head_node
        while current_node.pointer:
            if current_node.data == data:
                return True
            current_node = current_node.pointer
        return current_node.data == data

    def insert_tail(self, node):
        current_node = self.head_node
        # while the current nodes pointer points at the next node - we do this loop
        # While Flase - I'm not gonna run the indented line, I move on.
        # While some condition is true, we will run my block, once condition is false - we will move on to the next line
        # while loop is always looking for something true
        while current_node.pointer:
            current_node = current_node.pointer
        current_node.pointer = node

    def delete(self, data):
	"""
	Delete a node
	
	Figure out if it's head, mid, tail
	
	params:
		input is some data, we find the node, delete it if it's there
	return:
		could be static (does not return anything)
		could return a bool (true or false)
	
	"""

	current_node = self.head_node

	# HEAD NODE:
	# if the data is  equal to our current node
	if current_node.data == data
	    # self references the instance - and of the instance attributes are available in self
	    # whatever is on the left we assign too, and whatever is on the right is whatever we are going to assign it too.
	    self.head_node = current_node.pointer
	# SOMEWHERE IN THE MIDDLE NODE:
	# does my current node have a child, does that child have a child, if yes - continue to do something
	while current_node.pointer.pointer:
	    if current_node.pointer.data == data:
		current_node.pointer = currnet_node.pointer.pointer
	        return True
	# TAIL NODE:
	# is my next nodes data == to the data i passed in
	if current_node.pointer.data == data:
	   # set the reference of the current node (the next node) to none, aka tail
	   current_node.pointer = None
	   return True

	return False

    def update(self, data, new_data):
        """
        Search for a value inside of the link list, and set that value to a new value
        
        Params:
            value we are looking for
            value we want to replace it with


        return:
            True or False
            True if you are able to find and replace value
            False if you were not able to find and replace value

        """

        current_node = self.head_node
        while current_node.pointer:
            if current_node.data == data:
                current_node.data = new_data
                return True
            current_node = current_node.pointer 
        if current_node.data == data:
            current_node.data = new_data
            return True
        return False


# (head:node:peter)->(tail:node:doggyhorse)->
my_node = Node("peter")
my_linklist = Linklist(my_node) #(peter)->
my_tail_node = Node("doggyhorse")
my_linklist.insert_tail(my_tail_node)#(peter)->(doggyhorse)->
my_another_node = Node("horsecat")
my_linklist.insert_tail(my_another_node)

