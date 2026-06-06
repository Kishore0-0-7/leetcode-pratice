class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=curr=count=0
        while curr<len(nums):
            if nums[curr]==0:
                right=0
                for i in range(curr, len(nums)):
                    right+=nums[i]
                if left==right:
                    count+=2
                elif abs(left-right)==1:
                    count+=1
            else:
                left+=nums[curr]
            curr+=1
        return count