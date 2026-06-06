class Solution(object):
    def minArraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans=0
        for x in nums:
            b=x
            for y in nums:
                if y>x:
                    break
                if x%y==0:
                    b=y
                    break
            ans+=b
        return ans