class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        d1,d2=d
        r1,r2=r
        t=0
        while d1>0 or d2>0:
            t+=1
            can1=(t%r1!=0 and d1>0)
            can2=(t%r2!=0 and d2>0)
            if can1 and (not can2 or d1>=d2):
                d1-=1
            elif can2:
                d2-=1
        return t