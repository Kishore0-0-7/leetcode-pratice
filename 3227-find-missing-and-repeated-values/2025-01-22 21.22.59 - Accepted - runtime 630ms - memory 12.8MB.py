class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        new = []
        for i in grid:
            new.extend(i)
        for i in new:
            if new.count(i) == 2:
                a = i
                break
        for i in range(1, len(new) + 1):
            if i not in new:
                b = i
                break
        return [a, b]