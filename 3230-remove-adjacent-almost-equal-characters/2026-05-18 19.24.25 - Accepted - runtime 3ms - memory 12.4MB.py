class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans=0
        s=word
        n=len(s)
        i=1
        while i<n:
            if abs(ord(s[i])-ord(s[i-1]))==1 or s[i]==s[i-1]:
                ans+=1
                i+=1
            i+=1
        return ans