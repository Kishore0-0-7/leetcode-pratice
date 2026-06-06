class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        return sum(max(b - a, 0) for b, a in zip(target, [0] + target))