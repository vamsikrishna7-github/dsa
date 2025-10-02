class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, data):
        if not self.head:
            n = Node(data)
            self.head=n
            return
        
        n = Node(data,next=self.head)
        self.head = n
        return
    
    def insert_at_end(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            return
        n = Node(data)

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next=n
        return
    
    def insert_at_index(self, data, index):
        if not self.head:
            n = Node(data)
            self.head = n
        
        count = 1
        temp = self.head
        while temp.next:
            if count == index:
                break
            count +=1
            temp = temp.next
        temp.next= Node(data, next=temp.next)
        return
    
    def print_list(self):
        if self.head == None:
            print("list is empty")
            return
        n = self.head
        while n:
            print(n.data, " --> ", end="")
            n = n.next
        print()
    
    def list_size(self):
        if not self.head:
            return 0
        
        count = 1
        temp = self.head
        while temp.next:
            count +=1
            temp = temp.next
        return count
        
l = SingleLinkedList()
print("List Size is ", l.list_size())
l.insert_at_begin(10)
l.insert_at_begin(20)
l.insert_at_begin(30)
l.insert_at_end(40)
l.insert_at_begin(50)
l.insert_at_end(60)
l.print_list()
l.insert_at_index(333, 3)
l.print_list()
l.insert_at_index(111, 1)
l.print_list()
l.insert_at_index(555, 5)
l.print_list()
print("List Size is ", l.list_size())