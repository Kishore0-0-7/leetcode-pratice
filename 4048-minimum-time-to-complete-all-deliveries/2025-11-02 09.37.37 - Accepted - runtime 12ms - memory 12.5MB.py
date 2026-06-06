class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        d1,d2=d
        r1,r2=r
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        def lcm(a,b):
            return (a*b)//gcd(a,b)
        def cancomp(t):
            av1=t-t//r1
            av2=t-t//r2
            if av1<d1 or av2<d2:
                return False
            bb=t//lcm(r1,r2)
            md=t-bb
            return md>=d1+d2            
        left,right=1,2*(d1+d2+max(r1,r2))
        while left<right:
            mid=(left+right)//2
            if cancomp(mid):
                right=mid
            else:
                left=mid+1
        return left