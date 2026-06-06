# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums=set(nums)
        cur=head
        prev=None
        while cur:
            if cur.val in nums:
                if prev:
                    prev.next=cur.next
                    cur=cur.next
                else:
                    head=cur.next
                    cur=cur.next
            else:
                prev=cur
                cur=cur.next
        return head