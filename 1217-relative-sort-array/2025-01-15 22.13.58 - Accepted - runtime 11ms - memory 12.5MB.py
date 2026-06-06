class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        res = []
        for num in arr2:
            res.extend([num] * arr1.count(num))
        remaining = sorted(num for num in arr1 if num not in arr2)
        return res + remaining