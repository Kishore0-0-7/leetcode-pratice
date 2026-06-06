class Solution(object):
    def findMaxVal(self, n, restrictions, diff):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type diff: List[int]
        :rtype: int
        """
        inf=10**8
        mh=[inf]*n
        mh[0]=0
        for id,val in restrictions:
            mh[id]=min(mh[id],val)
        for i in range(1,n):
            mh[i]=min(mh[i],mh[i-1]+diff[i-1])
        for i in range(n-2,-1,-1):
            mh[i]=min(mh[i],mh[i+1]+diff[i])
        return max(mh)