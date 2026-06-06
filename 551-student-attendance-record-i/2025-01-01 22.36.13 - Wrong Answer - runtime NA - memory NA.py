class Solution(object):
    def checkRecord(self, s):
        c=0
        for i in s:
            if i=='L':
                c+=1
                if c>=3:
                    return False
        if s.count('A')>=2:
            return False
        return True
        