class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rightSum=sum(nums)
        leftSum=0
        ans=[]
        for num in nums:
            rightSum-=num
            ans.append(abs(leftSum-rightSum))
            leftSum+=num
        return ans