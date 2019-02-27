class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = id(link)


def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

def addtoLast(data):
    global head
    if head == None:
        head = Node(data, None)
    else:
        p = head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)


for _ in range(int(input())):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))

    head = None
    for i in range(5):
        if i == 0:
            Node(lst[i], head)
        else:
            Node(lst[i], )





    print(f'#{_+1}')