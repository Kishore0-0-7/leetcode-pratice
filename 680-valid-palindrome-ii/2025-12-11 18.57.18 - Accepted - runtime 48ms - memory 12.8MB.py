class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                sl=s[l+1:r+1]
                sr=s[l:r]
                return (sl==sl[::-1]) or (sr==sr[::-1])
        return True
 
