class Solution(object):
    def maximumScore(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        count_ones=s.count('1')
        nums.sort(reverse=True)
        return sum(nums[:count_ones])
        