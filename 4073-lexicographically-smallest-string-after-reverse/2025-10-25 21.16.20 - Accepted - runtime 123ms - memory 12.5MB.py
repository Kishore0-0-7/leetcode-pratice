class Solution(object):
    def lexSmallest(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=s
        n=len(s)
        for k in range(1,n+1):
            fr=s[:k][::-1]+s[k:]
            ls=s[:-k]+s[-k:][::-1]
            ans=min(ans,fr,ls)
        return ans