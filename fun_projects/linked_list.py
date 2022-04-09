class node:
    """
    an object to store a single node of a linked list 
    models 2 attributes a data and a link to the next node
    """
    data = None
    next_Node = None

    def __init__(self, data) :
       self.data = data


    def __repr__(self) :
       return "<Node data: %s>" % self.data  
class linkedList:
    def __init__(self) :
        self.head = None
    def is_empty(self):
        return self.head == None
    def size(self):
        current= self.head
        count = 0 
        while current:
            count+=1
            current = current.next_Node   

        return count 


    def add(self,data):
        new_node = node(data)
        new_node.next_Node = self.head
        self.head  = new_node
        """
        adds new node containing data at the head of the list this operation
        takes O(1)
        """           
   

