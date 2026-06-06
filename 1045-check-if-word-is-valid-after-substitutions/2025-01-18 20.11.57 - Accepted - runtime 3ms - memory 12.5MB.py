class Solution(object):
    def isValid(self, s):
        f=True
        while f:
            if "abc" in s:
                s=s.replace("abc","")
            else:
                f=False
        return s==""