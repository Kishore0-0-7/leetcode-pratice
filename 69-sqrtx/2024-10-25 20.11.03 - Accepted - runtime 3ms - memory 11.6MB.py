class Solution(object):
    def mySqrt(self, x):
        if x <2:
            return x
        a,b= 0,x
        while abs(a-b) != 1:
            mid = (a+b) // 2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                b = mid
            else:
                a = mid
        return a
        