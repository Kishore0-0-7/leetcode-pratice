class Solution(object):
    def checkRecord(self, s):
        if s.count('L')>=3:
            return False
        if s.count('A')>=2:
            return False
        return True
        