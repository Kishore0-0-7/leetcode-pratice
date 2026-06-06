class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        nums.sort()
        total=1
        if len(nums)==1:
            return nums[0]
        for num in nums:
            if num<0:
                count+=1
        if count<2 and max(nums)==0:
            return 0
        if count%2==0:
            for num in nums:
                if num!=0:
                    total*=num
            return total
        else:
            for num in nums:
                if count!=1:
                    if num!=0:
                        total*=num
                count-=1
            return total