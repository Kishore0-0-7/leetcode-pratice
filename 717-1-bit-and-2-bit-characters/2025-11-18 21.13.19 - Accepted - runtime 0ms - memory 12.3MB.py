class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i,n=0,len(bits)
        while i<n-1:
            i+=bits[i]+1
        return n-i==1