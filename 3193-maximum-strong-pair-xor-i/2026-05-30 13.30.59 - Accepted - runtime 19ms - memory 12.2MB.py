class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        Max=0
        for i,n1 in enumerate(nums):
            for n2 in nums[i+1:]:
                if n2-n1<=n1:
                    Max=max(Max,n1^n2)
                else:
                    break 
        return Max