class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        mas=sum(nums[-k:])
        mns=sum(nums[:k])
        return abs(mas-mns)