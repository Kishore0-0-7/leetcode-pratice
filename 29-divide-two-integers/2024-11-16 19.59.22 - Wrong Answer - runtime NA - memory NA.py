import math
class Solution(object):
    def divide(self, dividend, divisor):
        if (divisor>0 and dividend >0):
            return dividend//divisor
        if(dividend%divisor==0):
            return dividend/divisor
        return (dividend/divisor)+1