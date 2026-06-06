class Solution(object):
    def findOcurrences(self, text, first, second):
        third = []
        t = text.split()
        for i in range(len(t)-2):
            if t[i] == first and t[i+1] == second :
                third.append(t[i+2])
        return third