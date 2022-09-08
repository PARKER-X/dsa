# Linked list in python 
# Node ---> Data and next
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
# Linked List ----> Head + Node + Last Node(Next=None)

class LinkedList:
    def __init__(self):
        self.head = None
        
    # Insert at beginning
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        

    # Print linked list
    def printlist(self):
        if self.head is None:
            print("Empty linkedlist")
            return 
        itr = self.head
        llstr= ''
        while itr:
            if itr.next:
                llstr += str(itr.data) + ' --> '
            else:
                llstr += str(itr.data)
            itr = itr.next
        print(llstr)
        
    # Insert at  End of Linked List
    def insert_at_end(self, data):
        if self.head==None:
            node = Node(data, self.head)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        
    # Insert at any index of Linked List
    def insert_at(self, index, data):
        if index< 0:
            print("Invalid Index")
        if index==0:
            self.insert_at_beginning(data)
            return 
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1
            
    # length of linked list        
    def length(self):
        count=0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        print(count)
            
    # Insert at  Mid of Linked List       
    def insert_at_mid(self, data):
        count=0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        mid = count//2
        self.insert_at( mid,data)

    #Show Specific Element in list 
    def show(self, index):
        count = 0
        itr = self.head 
        while itr:
            if count == index:
                print(itr.data)
            itr = itr.next
            count +=1
        return None

    # Reverse the Linked List
    def reverse(self):
        itr = self.head 
        if itr is None:
            return 
        curr_node = self.head 
        prev_node = None

        while curr_node:
            next_node = curr_node.next 
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def delete(self, index):
        
        if index<0 and index>self.length():
            raise "Invalid Error"
            
        if  index==0:
            self.head = self.head.next 
            return
        
        count = 0
        itr = self.head 
        while itr:
            if count == index-1:
                itr.next = itr.next.next 
                break
            itr = itr.next 
            count+=1
        
        
   

       
            
            
        
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(100)
    ll.insert_at_beginning(5)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at(2,20)
    ll.insert_at(0,0)
    ll.insert_at(1,12)
    ll.insert_at_mid(111)
    ll.show(4)
    ll.reverse()
    ll.length()
    ll.delete(1)
    print(ll)
    ll.printlist()
    
    
    
       
            