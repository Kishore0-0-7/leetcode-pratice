# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dm1=odd=ListNode(0)
        dm2=even=ListNode(0)

        while head:
            odd.next=head
            even.next=head.next
            odd=odd.next
            even=even.next
            head=head.next.next if even else None

        odd.next=dm2.next
        return dm1.next