class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        l1=abs(x-z)
        l2=abs(y-z)
        if(l1>l2):
            return 2
        elif(l1<l2):
            return 1
        else:
            return 0
