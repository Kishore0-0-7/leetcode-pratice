class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        index=[]
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[j]==key and abs(i-j)<=k:
                    index.append(i)
                    break
        return index
