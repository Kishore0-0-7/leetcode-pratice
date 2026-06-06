class Solution(object):
    def numberOfLines(self, widths, s):
        tw=0
        l=1
        for i in s:
            w=widths[ord(i)-ord("a")]
            tw+=w
            if tw>100:
                l+=1
                tw=w
        return [l,tw]
        