class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        for i in range(n-1):
            dif=abs(int(s[i])-int(s[i+1]))
            if(dif>2): return False
        return True