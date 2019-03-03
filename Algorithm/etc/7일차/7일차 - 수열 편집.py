class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    def first(self):
        if self.num_of_data == 0:
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

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1
    
    def add(self, idx, data):
        new_node = Node(data)

        self.current = self.head
        temp = 0
        while temp < idx:
            if self.current.next:
                self.current = self.current.next
            temp += 1
        
        new_node.next = self.current.next
        self.current.next = new_node
        
        self.num_of_data += 1
    
    def delete(self, idx):
        temp = 0
        self.current = self.head

        while temp <= idx:
            if self.current.next:
                self.before = self.current
                self.current = self.current.next
            temp += 1

        self.before.next = self.current.next
        self.before = self.current

        self.num_of_data -= 1

    def change(self, idx, data):

        self.current = self.head

        temp = 0
        while temp <= idx:
            if self.current.next:
                self.current = self.current.next
            temp += 1

        self.current.data = data

    def size(self):
        return self.num_of_data


        
for _ in range(int(input())):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))

    l_lst = Linked_list()
    for i in lst:
        l_lst.append(i)
    
    for m in range(M):
        temp = list(input().split())
        if temp[0] == 'I':
            l_lst.add(int(temp[1]), int(temp[2]))
        elif temp[0] == 'D':
            l_lst.delete(int(temp[1]))
        else:
            l_lst.change(int(temp[1]), int(temp[2]))
    
    result = 0
    if l_lst.size() < L:
        result = -1
    else:
        data = l_lst.first()
        nums = []
        if data:
            nums.append(data)
            while 1:
                data = l_lst.next()
                if data:
                    nums.append(data)
                else:
                    break
        # print(nums)
        result = nums[L]
    print(f'#{_+1} {result}')