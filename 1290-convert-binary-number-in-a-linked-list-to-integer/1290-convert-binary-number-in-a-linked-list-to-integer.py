# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        res=0
        n=head
        c=-1
        while n:
            c+=1
            n=n.next
        temp=head
        while temp:
            if temp.val==1:
                res+=pow(2,c)
            c-=1
            temp=temp.next
        return res