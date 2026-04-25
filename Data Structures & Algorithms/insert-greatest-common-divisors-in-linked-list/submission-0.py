# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            nxt = cur.next
            gcd = math.gcd(cur.val, nxt.val)
            newNode = ListNode(gcd, nxt)
            cur.next = newNode
            cur = nxt
        return head
