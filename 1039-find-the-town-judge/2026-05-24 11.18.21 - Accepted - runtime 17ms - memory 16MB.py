class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n==1 and len(trust)==0:
            return 1
        count=[0]*(n+1)
        for (a,b) in trust:
            count[a]-=1
            count[b]+=1
        for i in range(len(count)):
            if count[i]==n-1: return i
        return -1