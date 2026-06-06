class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        l=[]
        for i in range(len(words1)):
            if (words2[0] in words1[i] and words2[1] in words1[i] ):
                l.append(words1[i])
        return l