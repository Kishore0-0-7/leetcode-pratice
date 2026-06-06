class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        def is_inc(arr):
            return all(arr[i]<arr[i+1] for i in range (len(arr)-1))
        def is_dec(arr):
                return all(arr[i]>arr[i+1] for i in range (len(arr)-1))
        mini=float("inf")
        found=False
        for i in range(n-1):
            left=nums[:i+1]
            right=nums[i+1:]
            if is_inc(left) and is_dec(right):
                d=abs(sum(left)-sum(right))
                mini=min(d,min)
                found=True
        return mini if found else -1