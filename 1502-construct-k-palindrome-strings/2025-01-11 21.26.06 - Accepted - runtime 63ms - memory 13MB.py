class Solution(object):
    def canConstruct(self, s, k):
        if len(s)<k:
            return False
        char = {}
        for i in s:
            if i in char:
                char[i]+=1
            else:
                char[i] = 1
        odd_count = 0
        for i in char.values():
            if i % 2 != 0:
                odd_count += 1
        return odd_count <= k