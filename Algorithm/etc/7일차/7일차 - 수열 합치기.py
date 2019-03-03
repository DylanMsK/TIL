# 무식하게
# for _ in range(int(input())):
#     N, M = map(int, input().split())
#     lst = []
#     for i in range(M):
#         temp = list(map(int, input().split()))
#         if lst:
#             for i in range(len(lst)):
#                 if lst[i] > temp[0]:
#                     lst = lst[:i] + temp + lst[i:]
#                     break
#             else:
#                 lst = lst + temp
#         else:
#             lst = temp

#     print(f'#{_+1} {" ".join([str(i) for i in lst[::-1][:10]])}')


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# TODO 더블 링크드리트로 새로만들기
class LinkedList:
    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0


    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    def add(self, idx, data):
        now = 0
        self.current = self.head

        while now < idx:
            if self.current.next:
                self.current = self.current.next
            now += 1
        
        new_node = Node(data)
        new_node.next = self.current.next
        self.current.next = new_node

        self.num_of_data += 1

    def data(self):
        return self.current.data
    
    def next(self):
        if self.current.next == None:
            return None

        self.current = self.current.next
        return self.current.data

    def first(self):
        if self.num_of_data == 0:
            return None
        
        # self.before = self.head
        self.current = self.head.next
        return self.current.data

    def search(self, idx):
        self.current = self.head
        temp = 0
        while temp <= idx:
            self.current = self.current.next
            temp += 1
        
        return self.current.data

    # def last(self):
    #     self.before = self.head
    #     self.current = self.head.next

    #     temp = 0
    #     while temp < self.num_of_data:
    #         self.current = self.current.next
    #         self.before = self.current

    #     return self.current.data


    # def before(self):
    #     self.current = self.before



    def size(self):
        return self.num_of_data


for _ in range(int(input())):
    N, M = map(int, input().split())
    l_lst = LinkedList()
    for i in range(M):
        temp = list(map(int, input().split()))
        if l_lst.size == 0:
            for j in temp:
                l_lst.append(j)
        else:
            idx = 0
            l_lst.first()
            for j in range(l_lst.size()):
                if l_lst.data():
                    if l_lst.data() > temp[0]:
                        break
                    l_lst.next()
                    idx += 1
            
            if idx == l_lst.size:
                for j in temp:
                    l_lst.append(j)
            else:
                for j in temp:
                    l_lst.add(idx, j)
                    idx += 1
    
    # l_lst.first()
    # temp = []
    # for i in range(l_lst.size()):
    #     temp.append(l_lst.data())
    #     l_lst.next()
    # temp = temp[-10:]

    nums = l_lst.size()
    temp = []
    for i in range(nums-1, nums-11, -1):
        temp.append(l_lst.search(i))

    print(f'#{_+1} {" ".join([str(i) for i in temp])}')