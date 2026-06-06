class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        n = len(s)
        l = list(s)
        for i in range(n):
            if t[i] in l:
                l.remove(t[i])
            else:
                return False
        return True