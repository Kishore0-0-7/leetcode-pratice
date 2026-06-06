class Solution(object):
    def findRelativeRanks(self, score):
        n=sorted(score,reverse=True)
        a=['']*len(score)
        for i in range(len(score)):
            p=n.index(score[i])+1
            if p == 1:
                a[i] = "Gold Medal"
            elif p == 2:
                a[i] = "Silver Medal"
            elif p == 3:
                a[i] = "Bronze Medal"
            else:
                a[i] = str(p)
        return a