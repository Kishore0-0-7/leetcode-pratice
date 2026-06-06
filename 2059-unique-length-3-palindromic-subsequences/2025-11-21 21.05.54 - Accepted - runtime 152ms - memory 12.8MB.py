class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        up=0
        for c in set(s):       
            l=s.find(c)
            r=s.rfind(c)
            if l<r:          
                middle_chars=set(s[l+1:r])
                up+=len(middle_chars)
        return up