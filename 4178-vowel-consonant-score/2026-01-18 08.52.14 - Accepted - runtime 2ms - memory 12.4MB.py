class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        vo=['a','e','i','o','u']
        v,c=0,0
        for ch in s:
            if ch in vo and ch.isalpha():
                v+=1
            elif ch.isalpha():
                c+=1
        return int(math.floor(v/c)) if c else 0