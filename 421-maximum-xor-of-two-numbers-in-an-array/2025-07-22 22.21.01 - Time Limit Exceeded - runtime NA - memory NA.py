class Solution(object):
    def findMaximumXOR(self, nums):
        max_xor = 0
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                max_xor = max(max_xor, nums[i] ^ nums[j])
        return max_xor
        