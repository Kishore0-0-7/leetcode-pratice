class Solution(object):
    def prefixConnected(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        mp=defaultdict(int)
        for w in words:
            if len(w)>=k:
                p=w[:k]
                mp[p]+=1
        res=0
        for c in mp.values():
            if c>=2:
                res+=1
        return res