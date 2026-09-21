# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==None or headB==None:
            return None 
        n=headA
        d={}
        while n:
            d[n]=1
            n=n.next
        b=headB
        while b:
            if b in d:
                return b
            b=b.next
        return None