class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.rstrip()
        if(len(s)-1==0):
            return 1
        i=len(s)-1
        while(i>0 and s[i]!=' '):
            i-=1
        return len(s)-i-1