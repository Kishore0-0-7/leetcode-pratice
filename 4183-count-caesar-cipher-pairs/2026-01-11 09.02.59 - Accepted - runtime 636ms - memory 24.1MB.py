class Solution(object):
    def countPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        freq=defaultdict(int)
        for word in words:
            base=ord(word[0])
            normalized=[]
            for c in word:
                shifted=(ord(c)-base+26)%26
                normalized.append(chr(shifted+ord('a')))
            key=''.join(normalized)
            freq[key]+=1
        ans = 0
        for k in freq.values():
            ans+=k*(k-1)//2
        return ans