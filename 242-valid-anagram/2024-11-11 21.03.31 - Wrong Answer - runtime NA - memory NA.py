class Solution(object):
    def isAnagram(self, s, t):
        for i in range((len(s)+len(t))/2):
            if s[i] not in t or t[i] not in s :
                return False
                break
        return True
        