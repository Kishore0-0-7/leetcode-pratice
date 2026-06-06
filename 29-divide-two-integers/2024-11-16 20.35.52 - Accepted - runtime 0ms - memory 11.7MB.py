import math
class Solution(object):
    def divide(self, dividend, divisor):
        if ((dividend<0 and divisor<0) or (divisor>0 and dividend >0)):
            d=dividend//divisor
            if(d>=2147483648):
                return d-1
            return d
        if(dividend%divisor==0):
            return dividend//divisor
        return (dividend/divisor)+1