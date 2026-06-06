class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lst=[]
        d={}
        for e in nums2:
            while(lst and e>lst[-1]):
                c=lst.pop()
                d[c]=e
            lst.append(e)
        return [d.get(e,-1) for e in nums1]