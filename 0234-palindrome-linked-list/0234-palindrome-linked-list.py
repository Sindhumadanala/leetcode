# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head:
            return head
        def reverse(new_head):
            prev=None
            n=new_head
            while n:
                temp=n.next
                n.next=prev
                prev=n
                n=temp
            return prev
        fast=head
        slow=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        new_head=slow.next
        org=head
        rev_ll=reverse(new_head)
        while rev_ll:
            if org.val!=rev_ll.val:
                return False
            org=org.next
            rev_ll=rev_ll.next
        return True

            