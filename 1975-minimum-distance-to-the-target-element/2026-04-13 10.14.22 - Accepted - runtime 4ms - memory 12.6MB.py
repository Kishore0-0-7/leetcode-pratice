class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        l=[]
        k=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        for i in l:
            k.append(abs(i-start))
        return min(k)