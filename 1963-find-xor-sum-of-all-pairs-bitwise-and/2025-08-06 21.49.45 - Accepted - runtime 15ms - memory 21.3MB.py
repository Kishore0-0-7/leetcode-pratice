class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        ans1 = 0
        ans2 = 0
        for num in arr1:
            ans1 ^= num
        for num in arr2:
            ans2 ^= num
        return ans1 & ans2