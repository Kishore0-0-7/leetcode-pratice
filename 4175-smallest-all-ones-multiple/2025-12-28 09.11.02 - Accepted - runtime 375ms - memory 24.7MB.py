class Solution(object):
    def minAllOneMultiple(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k%2==0 or k%5==0:
            return -1
        r=0
        seen=set()
        for l in range(1,k+1):
            r=(r*10+1)%k
            if r==0:
                return l
            if r==0:
                return l
            if r in seen:
                return -1
            seen.add(r)
        return -1