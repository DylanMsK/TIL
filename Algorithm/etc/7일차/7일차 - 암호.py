class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.first = None
        self.curr = None
        self.prev = None
        self.num_of_data = 0

    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
        self.num_of_data += 1

    def append(self, data):
        new_node = Node(data)
        if self.first == None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.num_of_data += 1
        else:
            self.insert_after(self.first.prev, new_node)
    
    def first(self):
        if self.first == None:
            self.curr = self.first
            self.prev = self.first
        else:
            self.curr = self.first.next
            self.prev = self.first.prev
            self.next = self.first.next.next

    def insert_middle(self, step):
        while step != 0:
            self.prev = self.curr
            self.curr = self.curr.next
            self.next = self.curr.next.next
            step -= 1
        
        if self.curr.next == self.first:
            data = self.first.data + self.first.prev.data
            new_node = Node(data)
            self.insert_after(self.first.prev, new_node)
        else:
            data = self.prev.data + self.next.data
            new_node = Node(data)
            self.insert_after(self.prev, new_node)
        self.num_of_data += 1

    def next(self):
        self.prev = self.curr
        self.curr = self.curr.next
        self.next = self.curr.next

    def display(self):
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.first:
                break

    def size(self):
        return self.num_of_data





for _ in range(int(input())):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    l_lst = CircularLinkedList()
    for i in lst:
        l_lst.append(i)
    
    
    l_lst.display()


    # while K != 0:
    #     l_lst.insert_middle(M)
    #     K -= 1
    # result = []
    # l_lst.first()
    # for i in range(l_lst.size()):
    #     result.append(l_lst.curr.data)


    # print(f'#{_+1} {result}')