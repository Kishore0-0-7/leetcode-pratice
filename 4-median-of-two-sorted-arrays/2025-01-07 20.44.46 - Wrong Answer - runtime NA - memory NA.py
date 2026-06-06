class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num=list(set(nums1+nums2))
        n=sum(num)
        mn=float(n)
        mn=mn/len(num)
        return mn