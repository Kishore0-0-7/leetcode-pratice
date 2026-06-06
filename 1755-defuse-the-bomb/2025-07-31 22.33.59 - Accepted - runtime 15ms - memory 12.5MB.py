class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        result = []

        for i in range(n):
            if k == 0:
                result.append(0)
            elif k > 0:
                list1 = []
                for j in range(1, k + 1):
                    index = (i + j) % n
                    list1.append(code[index])
                result.append(sum(list1))
            else:
                list1 = []
                for j in range(1, abs(k) + 1):
                    index = (i - j + n) % n
                    list1.append(code[index])
                result.append(sum(list1))

        return result