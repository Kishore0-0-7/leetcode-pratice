class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        s , t = sorted(s) , sorted(t)
        if s==t:
            return True
        return False
        