class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        total=0
        prev=0
        for i in bank:
            current=0
            for j in i:
                current+=1 if j=="1" else 0
            if(current>0):
                total+=current*prev
                prev=current
        return total