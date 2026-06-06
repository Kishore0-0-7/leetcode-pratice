from collections import deque

class Solution(object):
    def countSubarrays(self, nums, k):
        maxD=deque()
        minD=deque()
        l=0
        ans=0
        for r in range(len(nums)):
            while maxD and maxD[-1]<nums[r]:
                maxD.pop()
            maxD.append(nums[r])
            while minD and minD[-1]>nums[r]:
                minD.pop()
            minD.append(nums[r])
            while (maxD[0]-minD[0])*(r-l+1)>k:
                if nums[l]==maxD[0]:
                    maxD.popleft()
                if nums[l]==minD[0]:
                    minD.popleft()
                l+=1
            ans+=r-l+1
        return ans