class Solution(object):
    def mirrorFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        freq=Counter(s)
        v=set()
        ans=0
        for c in freq:
            if c in v:
                continue
            if c.isalpha():
                m=chr(ord('z')-(ord(c)-ord('a')))
            else:
                m=chr(ord('9')-(ord(c)-ord('0')))
            f1=freq[c]
            f2=freq.get(m,0)
            ans+=abs(f1-f2)
            v.add(c)
            v.add(m)
        return ans