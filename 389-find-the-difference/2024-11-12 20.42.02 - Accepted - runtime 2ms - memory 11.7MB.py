class Solution(object):
    def findTheDifference(self, s, t):
        a=sum([ord(i) for i in s])
        b=sum([ord(i) for i in t])
        c=abs(a-b)
        return chr(c)