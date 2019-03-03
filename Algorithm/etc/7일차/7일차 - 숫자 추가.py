class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        dummy = Node('dummy')

        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_date = 0

    
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_date += 1

    def search(self, idx):
        self.current = self.head
        temp = 0
        while temp <= idx:
            self.current = self.current.next
            temp += 1
        
        return self.current.data


    def add(self, idx, data):
        new_node = Node(data)

        self.current = self.head
        temp = 0
        while temp < idx:
            self.current = self.current.next
            temp += 1
        
        new_node.next = self.current.next
        self.current.next = new_node
        
        self.num_of_date += 1


    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:       # 이거는 왜????
            self.before = self.tail

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_date -= 1
        return pop_data


    def first(self):
        if self.num_of_date == 0:
            return None
        
        self.before = self.head
        self.current = self.head.next

        return self.current.data


    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_date


for _ in range(int(input())):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))

    l_lst = LinkedList()
    for i in lst:
        l_lst.append(i)

    for i in range(M):
        a, b = map(int, input().split())
        l_lst.add(a, b)

    # data = l_lst.first()
    # temp = []
    # if data:
    #     temp.append(data)
    #     while 1:
    #         data = l_lst.next()
    #         if data:
    #             temp.append(data)
    #         else:
    #             break
    # print(temp)



    print(f'#{_+1} {l_lst.search(L)}')