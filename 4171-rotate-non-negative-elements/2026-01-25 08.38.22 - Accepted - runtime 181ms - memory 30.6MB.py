class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pos=[x for x in nums if x >= 0]
        if not pos:
            return nums
        k%=len(pos)
        pos=pos[k:]+pos[:k]
        j=0
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=pos[j]
                j+=1
        return nums