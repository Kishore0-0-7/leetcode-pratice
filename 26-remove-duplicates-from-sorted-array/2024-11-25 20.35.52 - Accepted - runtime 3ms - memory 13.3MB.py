class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        prev_val = nums[0] - 1
        for i in range(len(nums)):
            nums[k] = nums[i]
            if nums[i] != prev_val:
                k += 1
            prev_val = nums[i]

        return k