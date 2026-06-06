class Solution(object):
    def rotateString(self, s, goal):
        if (len(s)!=len(goal)):
            return false
        return (goal in (s+s))
        