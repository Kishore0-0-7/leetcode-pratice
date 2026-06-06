class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        c0=s.count('0')
        c1=s.count('1')
        ml=2*min(c0,c1)
        if ml==0:
            return 0
        l,z,o,res=0,0,0,0
        for r in range(n):
            if s[r]=='0':
                z+=1
            else:
                o+=1
            while abs(z-o)>1:
                if s[l]=='0':
                    z-=1
                else:
                    o-=1
                l+=1
            res=max(res,r-l+1)
        return min(ml,res)