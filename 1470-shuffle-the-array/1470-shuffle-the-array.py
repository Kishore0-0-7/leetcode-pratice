class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        list=[]
        for i in range(n):
            list.append(nums[i])
            list.append(nums[i+n])
        return list