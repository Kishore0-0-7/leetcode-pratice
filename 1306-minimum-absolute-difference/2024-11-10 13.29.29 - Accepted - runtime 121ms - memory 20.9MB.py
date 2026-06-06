class Solution(object):
    def minimumAbsDifference(self,arr):
        arr.sort()
        mi = float('inf')
        result = []
        for i in range(1, len(arr)):
            di = arr[i] - arr[i - 1]
            mi = min(mi, di)
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == mi:
                result = result + ([[arr[i - 1], arr[i]]])
        return result