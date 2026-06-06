class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt
        