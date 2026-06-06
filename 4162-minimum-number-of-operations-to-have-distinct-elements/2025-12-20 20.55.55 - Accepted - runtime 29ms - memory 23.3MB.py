class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in seen:
                return(i//3)+1
            seen.add(nums[i])
        return 0
        # op=0
        # n=len(nums)
        # i=0
        # while i<n:
        #     rem=nums[i:]
        #     if len(set(rem))==len(rem):
        #         break
        #     op+=1
        #     i+=3
        # return op















      