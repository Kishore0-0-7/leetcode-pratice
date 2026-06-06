class Solution(object):
    def countGoodRectangles(self, rectangles):
        t = {}
        for r in rectangles:
            p = min(r)
            if p in t:
                t[p] += 1
            else:
                t[p] = 1
        return t[max(t.keys())]
        