class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        n=len(nums)
        if n<k:
            return False
        found=0
        i=0
        while i+k<=n:
            increasing=True
            for j in range(i+1,i+k):
                if nums[j]<=nums[j-1]:
                    increasing=False
                    break
            if increasing:
                found+=1
                if found==2:
                    return True
                i+=k
            else:
                i+=1
        return False
