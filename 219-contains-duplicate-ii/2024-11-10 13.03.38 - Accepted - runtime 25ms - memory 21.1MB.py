class Solution(object):
    def containsNearbyDuplicate(self,nums, k):
        s= {}
        for i, num in enumerate(nums):
            if num in s:
                if i - s[num] <= k:
                    return True
                    break
            s[num] = i
        return False        