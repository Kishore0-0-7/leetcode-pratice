class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        
        return res