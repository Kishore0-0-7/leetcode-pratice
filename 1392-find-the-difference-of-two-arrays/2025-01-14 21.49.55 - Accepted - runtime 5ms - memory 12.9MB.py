class Solution(object):
    def findDifference(self, nums1, nums2):
        n1=set(nums1)
        n2=set(nums2)
        u1=n1-n2
        u2=n2-n1
        return [list(u1),list(u2)]