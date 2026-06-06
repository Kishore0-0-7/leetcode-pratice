class Solution(object):
    def countDistinct(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen=set()
        for i in range(1,n+1):
            s=str(i).replace("0","")
            seen.add(s)
        return len(seen)