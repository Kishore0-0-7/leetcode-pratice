class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        temp=n
        mask=0
        while temp>0:
            mask=(mask<<1)|1
            temp>>=1
        return n^mask