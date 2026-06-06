class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s)
        l=len(s)
        while l>2:
            for i in range(l-1):
                s[i]=str((int(s[i])+int(s[i+1]))%10)
            l-=1
            print(s)
        return s[0]==s[1]