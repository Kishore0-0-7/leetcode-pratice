class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        count = 0
        for num in nums:
            if num % 6 == 0:
                total += num
                count += 1
        return 0 if count == 0 else total // count 