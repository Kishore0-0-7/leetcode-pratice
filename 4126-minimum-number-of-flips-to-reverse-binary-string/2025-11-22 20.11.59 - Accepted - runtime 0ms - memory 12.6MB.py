class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=bin(n)[2:]
        r=s[::-1]
        c=0
        for i in range(len(s)):
            if s[i]!=r[i]:
                c+=1
        return c