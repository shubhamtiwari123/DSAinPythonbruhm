class singlylinkedlist:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        se;

    def __str__(self):
        return str(self.val)


Head = singlylinkedlist(4)
A = singlylinkedlist(5)
B = singlylinkedlist(6)
C = singlylinkedlist(2)

Head.next = A
A.next = B
B.next = C

curr = Head
while curr:
    print(curr)
    curr = curr.next
