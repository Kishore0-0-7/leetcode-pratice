class Solution(object):
    def doesValidArrayExist(self, derived):
        res = 0
        for n in derived:
            res ^= n
        return res == 0