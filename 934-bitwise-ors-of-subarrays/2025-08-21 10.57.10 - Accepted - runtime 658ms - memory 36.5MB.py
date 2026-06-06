class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        cur = set()
        for num in arr:
            cur = {num | x for x in cur} | {num}
            res |= cur
        return len(res)