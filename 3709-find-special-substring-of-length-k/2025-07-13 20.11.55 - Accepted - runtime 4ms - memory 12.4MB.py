class Solution(object):
    def hasSpecialSubstring(self, s, k):
        if k >= len(s):
            if s==s[0]*k:
                return True
            return False 
        i=0 
        while i < len(s):
            c=s[i]
            j=i+1
            while j < len(s):
                if s[j]==s[i]:
                    c+=s[j]
                    j+=1
                else :
                    break 
            if len(c)==k :
                return True
            i=j
        return False 