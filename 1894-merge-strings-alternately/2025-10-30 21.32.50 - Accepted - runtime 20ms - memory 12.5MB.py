class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n=min(len(word1),len(word2))
        res=""
        for i in range(n):
            res+=word1[i]+word2[i]
        res+=word1[n:]+word2[n:]
        return res
        