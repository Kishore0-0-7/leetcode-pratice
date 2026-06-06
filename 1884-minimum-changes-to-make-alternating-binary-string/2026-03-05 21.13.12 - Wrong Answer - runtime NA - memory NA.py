class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        z,o=0,0
        for i in s:
            if i=="1": o+=1
            else: z+=1
        return (abs(z-o)//2)