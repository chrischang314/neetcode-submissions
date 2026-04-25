class Node:
    def __init__(self):
        self.val = None
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node()
    
    def get(self, index: int) -> int:
        cur = self.head.next
        if not cur:
            return -1
        for i in range(index):
            if not cur.next:
                return -1
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        newNode = Node()
        newNode.val = val
        newNode.next = self.head.next
        self.head.next = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node()
        newNode.val = val
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode

    def remove(self, index: int) -> bool:
        prv, cur = self.head, self.head.next
        if not cur:
            return False
        for i in range(index):
            if not cur.next:
                return False
            cur = cur.next
            prv = prv.next
        prv.next = cur.next
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
            

