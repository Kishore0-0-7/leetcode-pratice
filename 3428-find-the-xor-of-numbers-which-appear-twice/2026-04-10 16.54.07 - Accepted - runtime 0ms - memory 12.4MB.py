class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cm={}
        for i in nums:
            cm[i]=cm.get(i,0)+1
        c=0
        for k,v in cm.items():
            if v==2:
                c^=k
        return c
        