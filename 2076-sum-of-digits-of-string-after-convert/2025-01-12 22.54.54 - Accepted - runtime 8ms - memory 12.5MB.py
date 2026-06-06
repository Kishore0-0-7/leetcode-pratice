class Solution(object):
    def getLucky(self, s, k):
        number = ''
        for x in s:
            number += str(ord(x) - ord('a') + 1)
        
        for i in range(k):
            temp = 0
            for x in number:
                temp += int(x)
            number = str(temp) 
        return int(number) 