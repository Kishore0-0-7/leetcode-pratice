class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(num + 1):
            rev = int(str(i)[::-1])
            if i + rev == num:
                return True
        return False