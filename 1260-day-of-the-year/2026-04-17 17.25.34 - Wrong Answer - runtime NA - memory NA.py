class Solution(object):
    def dayOfYear(self,date):
        """
        :type date: str
        :rtype: int
        """
        dates=date.split('-')
        year,month,day=int(dates[0]),int(dates[1]),int(dates[2])
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
        countDays=day
        i=0
        while i<month-1:
            countDays+=months[i]
            i+=1
        if i>=2 and year%4==0 :
            countDays+=1
        return countDays