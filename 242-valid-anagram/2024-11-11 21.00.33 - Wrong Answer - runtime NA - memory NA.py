class Solution(object):
    def isAnagram(self, s, t):
        for i in t:
            if i not in s:
                return False
                break
        return True
        