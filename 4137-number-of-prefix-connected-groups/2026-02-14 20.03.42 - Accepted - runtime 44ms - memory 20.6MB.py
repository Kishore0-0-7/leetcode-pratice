class Solution(object):
    def prefixConnected(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: int
        """
        prefix_count={}
        for word in words:
            if len(word)>=k:
                prefix=word[:k]
                prefix_count[prefix]=prefix_count.get(prefix,0)+1
        groups=0
        for count in prefix_count.values():
            if count>=2:
                groups+=1
        return groups