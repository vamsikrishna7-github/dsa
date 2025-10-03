class Node:
    def __init__(self, pre=None, data=None, next=None):
        self.pre = pre
        self.data = data
        self.next = next

class Dlist:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(pre=temp ,data=data)
        return
    
    def create_list(self, l):
        for n in l:
            self.insert_end(n)
        return

    def print_list(self):
        if not self.head:
            print("List is empty!")
        
        temp = self.head
        while temp:
            print(temp.data, " <--> ", end="")
            temp = temp.next
        print()
        return
    
    def print_list_revrse(self):
        if not self.head:
            print("List is empty!")
        
        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, " <--> ", end="")
            temp = temp.pre
        print()
        return
    
    def inser_at_start(self, data):
        if not self.head:
            self.head = Node(data=data)
            return

        newnode = Node(data=data, next=self.head)
        self.head.pre = newnode
        self.head = newnode
        return
    
    def insert_at_index(self, data, index):
        
        newnode = Node(data=data)
        count = 0
        temp = self.head
        while temp:
            if count == index:
                x = temp.pre
                newnode.pre = x
                newnode.next = temp
                x.next = newnode
                temp.pre = newnode
            count +=1
            temp = temp.next
        return

dl = Dlist()
dl.create_list(["vamsi", "krishna", "nagid", "nagarjuna", "rajini", "rani", "nagesh", "sukumar"])
# dl.print_list()
# dl.print_list_revrse()
# dl.inser_at_start(100)
# dl.print_list()
# dl.print_list_revrse()
dl.insert_at_index("newnode", 0)
dl.print_list()