# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        t=head
        c=1
        while(t.next!=None):
            c+=1
            t=t.next
        # print(c)
        t.next=head
        n=c-k%c
        h=head
        # print(n)
        for i in range(n-1):
            # print(h.next.val)
            h=h.next
        # print(h.val)
        head=h.next
        h.next=None
        return head