class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxindex=0
        count=0
        maxcount=0
        startindex=-1
        for i in range(len(nums)):
            if(nums[i]==1):
                count+=1
            maxcount=max(maxcount,count)
            if(count==maxcount):
                maxindex=i-1
                startindex=maxindex-count+1
            if nums[i]==0:
                count=0
        print(maxindex)
        print(startindex)
        count=0
        for i in range(startindex,len(nums)):
            if i==(maxindex+1):
                continue
            if(nums[i]==1):
                count+=1
            if(nums[i]==0): break
        return count if(count<len(nums)) else count-1
            