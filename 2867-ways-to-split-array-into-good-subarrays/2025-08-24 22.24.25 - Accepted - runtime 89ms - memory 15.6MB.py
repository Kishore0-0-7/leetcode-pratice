class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        cnt = 0
        lo = -1
        for hi, b in enumerate(nums):
            if b == 1:
                if cnt == 0:
                    cnt = 1
                else:
                    cnt *= hi - lo
                    cnt %= 10 ** 9 + 7
                lo = hi
        return cnt