class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        a = s1.split()
        b = s2.split()
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in b:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        e = []
        for k,v in d.items():
            if v == 1:
                e.append(k)
        return e