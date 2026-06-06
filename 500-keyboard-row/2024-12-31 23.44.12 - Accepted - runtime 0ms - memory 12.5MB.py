class Solution(object):
    def findWords(self, words):
        a="qwertyuiopQWERTYUIOP"
        b="asdfghjklASDFGHJKL"
        c="zxcvbnmZXCVBNM"
        return [x for x in words if set(x).issubset(a) or set(x).issubset(b) or set(x).issubset(c) ]
        