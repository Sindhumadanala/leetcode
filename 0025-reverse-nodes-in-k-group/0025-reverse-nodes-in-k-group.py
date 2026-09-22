# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def reverseLinkedList(node):
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        def getKthNode(temp, steps):
            steps -= 1
            while temp is not None and steps > 0:
                temp = temp.next
                steps -= 1
            return temp

        temp = head
        prevNode = None

        while temp is not None:

            kthNode = getKthNode(temp, k)

            if kthNode is None:
                if prevNode:
                    prevNode.next = temp
                break

            nextNode = kthNode.next

            kthNode.next = None

            reverseLinkedList(temp)

            if temp == head:

                head = kthNode
            else:

                prevNode.next = kthNode

            prevNode = temp
            temp = nextNode

        return head
