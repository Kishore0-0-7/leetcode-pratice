class Solution(object):
    def reverseWords(self, s):
        w=s.split()
        k=[i[::-1] for i in w]
        return ' '.join(k)