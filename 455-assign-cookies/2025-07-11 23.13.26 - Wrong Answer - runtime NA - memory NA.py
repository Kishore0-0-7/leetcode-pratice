class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i,j,count=0,0,0
        g=sorted(g)
        s=sorted(s)
        while(i<len(g) and j<len(s)):
            if s[i]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count