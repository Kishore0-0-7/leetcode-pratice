class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans=""
        lst=[]
        for word in words:
            c=0
            for ch in word:
                c+=weights[ord(ch)-ord('a')]
            ans+=(chr(ord('z')-(c%26)))
        return ans