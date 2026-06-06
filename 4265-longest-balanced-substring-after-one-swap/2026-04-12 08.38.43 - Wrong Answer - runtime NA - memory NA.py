class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        arr=[1 if c=="1" else -1 for c in s]
        pre=0
        mp={0:-1}
        res=0
        for i in range(n):
            pre+=arr[i]
            if pre in mp:
                res+=max(res,i-mp[pre])
            else:
                mp[pre]=i
        c0=s.count('0')
        c1=s.count('1')
        maxpos=2*min(c0,c1)
        return min(maxpos,res+2)