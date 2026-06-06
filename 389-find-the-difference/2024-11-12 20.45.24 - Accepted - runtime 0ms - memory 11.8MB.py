class Solution(object):
    def findTheDifference(self, s, t):
        r= 0
        for c in s:
            r= r^ord(c)
        for c in t:
            r= r^ord(c)
        return chr(r)