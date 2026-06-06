class Solution(object):
    def countArrays(self, original, bounds):
        """
        :type original: List[int]
        :type bounds: List[List[int]]
        :rtype: int
        """
        n = len(original)
        left, right = bounds[0][0], bounds[0][1]
        for i in range(1, n):
            diff = original[i] - original[0]
            left = max(left, bounds[i][0] - diff)
            right = min(right, bounds[i][1] - diff)
        return max(0, right - left + 1)