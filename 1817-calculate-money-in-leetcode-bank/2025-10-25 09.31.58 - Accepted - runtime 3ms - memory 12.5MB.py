class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=c=t=0
        for i in range(n):
            if c==7:
                c=0
                m=i//7+1
            else:
                m+=1
            t+=m
            c+=1
        return t