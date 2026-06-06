class Solution(object):
    def isHappy(self, n):
        se= set()
        while (n not in se and n != 1):
            se.add(n)
            digits = (int(char) for char in str(n))
            total = 0
            for digit in digits:
                total += digit*digit
            n = total
        return n == 1