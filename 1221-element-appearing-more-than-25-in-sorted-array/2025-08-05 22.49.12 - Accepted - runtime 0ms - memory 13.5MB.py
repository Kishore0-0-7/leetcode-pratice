class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        quarter = n // 4

        for i in range(n - quarter):
            if arr[i] == arr[i + quarter]:
                return arr[i]