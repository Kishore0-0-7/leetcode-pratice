class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        a=word[0]
        res=1
        for i in range(1,n):
            if a==word[i]:
                res+=1
            a=word[i]
        return res