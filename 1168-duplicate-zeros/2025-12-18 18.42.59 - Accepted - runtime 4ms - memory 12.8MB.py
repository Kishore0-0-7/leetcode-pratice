class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i=0
        n=len(arr)
        while i<n:
            if arr[i]==0:
                arr.pop()
                arr.insert(i+1,0)
                i+=2
            else:
                i+=1