class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        lst = []

        for i in operations:
            if i == "C":
                lst.pop()
            elif i == "D":
                lst.append(2 * lst[-1])
            elif i == "+":
                lst.append(lst[-1] + lst[-2])
            else:
                lst.append(int(i))

        return sum(lst)