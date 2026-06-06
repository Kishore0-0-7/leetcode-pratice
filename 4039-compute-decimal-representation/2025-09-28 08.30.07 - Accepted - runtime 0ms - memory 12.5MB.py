class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst=[]
        p=1
        while n>0:
            d=n%10
            if d!=0:
                lst.append(d*p)
            n//=10
            p*=10
        return sorted(lst,reverse=True)