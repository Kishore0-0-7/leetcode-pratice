class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        cnt1 = cnt2 = 0
        for x in nums1:
            if x in s2:
                cnt1 += 1
        for y in nums2:
            if y in s1:
                cnt2 += 1
        lst = [0] * 2
        lst[0] = cnt1
        lst[1] = cnt2
        return lst