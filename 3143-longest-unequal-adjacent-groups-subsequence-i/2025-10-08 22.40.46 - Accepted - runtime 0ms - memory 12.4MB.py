class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        list1=[]
        list1.append(words[0])
        for i in range(1,len(groups)):
            if groups[i-1]!=groups[i]:
                list1.append(words[i])
        return list1