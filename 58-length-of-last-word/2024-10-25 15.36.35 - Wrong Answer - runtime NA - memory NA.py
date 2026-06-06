class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.rstrip()
        i=len(s)-1
        while(i>0 and s[i]!=' '):
            i-=1
        return len(s)-i-1