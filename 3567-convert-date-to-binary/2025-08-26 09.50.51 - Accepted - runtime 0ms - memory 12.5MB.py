class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        lst=date.split("-")
        return "-".join([bin(int(lst[0]))[2:],bin(int(lst[1]))[2:],bin(int(lst[2]))[2:]])