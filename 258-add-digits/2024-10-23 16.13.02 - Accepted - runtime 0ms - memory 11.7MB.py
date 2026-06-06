class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if (num==0):
            return 0
        a=1+((num-1)%9)
        return a