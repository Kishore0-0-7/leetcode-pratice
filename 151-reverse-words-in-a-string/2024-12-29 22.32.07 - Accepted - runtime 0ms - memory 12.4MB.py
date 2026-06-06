class Solution(object):
    def reverseWords(self, s):
        st=s.split()
        return ' '.join(st[::-1])
        