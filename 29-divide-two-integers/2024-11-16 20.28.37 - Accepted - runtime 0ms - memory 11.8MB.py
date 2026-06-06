import math
class Solution(object):
    def divide(self, dividend, divisor):
        if (dividend<0 and divisor<0):
            divisor=divisor*-1
            dividend=dividend*-1
            d=dividend//divisor
            if(d>=2147483648):
                return (dividend//divisor)-1
            return dividend//divisor
        if (divisor>0 and dividend >0):
            return dividend//divisor
        if(dividend%divisor==0):
            return dividend/divisor
        return (dividend/divisor)+1