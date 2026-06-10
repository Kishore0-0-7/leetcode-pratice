class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=len(s)
        k=k%n
        result=""
        for i in range(n):
            result+=s[(i+k)%n]
        return result