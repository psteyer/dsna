class Node:
    def __init__(self, data, next_pointer=None, prev_pointer=None):
        self.data = data
        self.next_pointer = next_pointer
        self.prev_pointer = prev_pointer


class Linkedlist:
    def __init__(self, head_node):
        self.head_node = head_node

    
    def search(self, data):
        current_node = self.head_node 
        while current_node.pointer:
            if current_node.data == data:
                return True
            current_node = current_node.pointer
        return current_node.data == data

    def replace():
        pass

    def delete():
        pass

    def delete_head():
        pass

    def delete_tail():
        pass

    def append(self, node):
        current_node = self.head_node
        
        while current_node.next_pointer:
            current_node = current_node.next_pointer
        # setting current_node's next pointer to the instatiation of a node
        current_node.next_pointer = node
        # setting our next nodes previous_pointer to ourselves aka current node. At this point we are still at second to last node. We never reach the end, because once we do we add.
        node.prev_pointer = current_node
        
    #TODO: Homework
    def insert_head():
        pass



