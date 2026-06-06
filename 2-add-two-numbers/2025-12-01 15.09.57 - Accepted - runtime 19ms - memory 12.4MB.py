# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s1=""
        head1=l1
        s2=""
        head2=l2
        while(head1!=None and head2!=None): 
            s1=str(head1.val)+s1
            head1=head1.next
            s2=str(head2.val)+s2
            head2=head2.next
        while(head1!=None): 
            s1=str(head1.val)+s1
            head1=head1.next
        while(head2!=None): 
            s2=str(head2.val)+s2
            head2=head2.next
        lst=[int(x) for x in list(str(int(s1)+int(s2)))][::-1]
        head=ListNode(lst[0])
        f=head
        for i in range(1,len(lst)):
            temp=ListNode(lst[i])
            head.next=temp
            head=head.next
        return f
        