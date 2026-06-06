class Solution(object):
    def rob(self, nums, colors):
        """
        :type nums: List[int]
        :type colors: List[int]
        :rtype: int
        """
        n = len(nums)
        torunelixa = (nums, colors)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = nums[0]

        if colors[1] == colors[0]:
            prev1 = max(nums[0], nums[1])
        else:
            prev1 = nums[0] + nums[1]

        for i in range(2, n):
            skip = prev1

            if colors[i] == colors[i - 1]:
                take = nums[i] + prev2
            else:
                take = nums[i] + prev1

            curr = max(skip, take)
            prev2 = prev1
            prev1 = curr

        return prev1