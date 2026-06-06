class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums)):
            mpp = {}
            pairs = 0
            for j in range(i, len(nums)):
                pairs += mpp.get(nums[j], 0)
                mpp[nums[j]] = mpp.get(nums[j], 0) + 1
                if pairs >= k:
                    cnt += 1
        return cnt