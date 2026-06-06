class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        r=0
        for c in s:
            d[c]=d.get(c,0)+1
        # print(d)
        for v in d.values():
            # print("before: ",v,r)
            r+=v if v%2==0 else v-1
            # print("after: ",v,r)
        return r+1 if r<len(s) else r