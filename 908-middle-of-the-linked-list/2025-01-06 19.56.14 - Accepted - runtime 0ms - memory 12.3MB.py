class Solution(object):
    def middleNode(self, head):
        lst=[]
        while head:
            lst.append(head)
            head=head.next
        m=len(lst)//2
        return lst[m]