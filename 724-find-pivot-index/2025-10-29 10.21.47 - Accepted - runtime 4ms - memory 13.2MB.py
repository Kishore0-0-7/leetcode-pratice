class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=0
        rs=sum(nums)
        for i,el in enumerate(nums):
            rs-=el
            if ls==rs:
                return i
            ls+=el
        return -1