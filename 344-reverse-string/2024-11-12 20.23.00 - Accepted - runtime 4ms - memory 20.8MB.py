class Solution(object):
    def reverseString(self, s):
       st=''
       n=len(s)-1
       i=0
       for i in range(0,len(s)):
            store = s[i]
            s[i]  = s[n]
            s[n]  = store 
            n = n-1  
            if i>=n:
                break