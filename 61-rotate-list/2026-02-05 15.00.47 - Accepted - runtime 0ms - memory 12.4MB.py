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
        if(not head):
            return head
        while(t.next!=None):
            c+=1
            t=t.next
        t.next=head
        n=c-k%c
        h=head
        for i in range(n-1):
            h=h.next
        head=h.next
        h.next=None
        return head