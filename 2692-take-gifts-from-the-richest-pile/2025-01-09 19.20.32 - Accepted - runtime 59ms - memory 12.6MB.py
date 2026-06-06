class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(k):
            gifts = sorted(gifts)
            sqrt = math.floor(math.sqrt(gifts[-1]))
            gifts[-1] = sqrt
        return int(sum(gifts))
        