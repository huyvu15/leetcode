class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        day = int(date[8:10])
        month = int(date[5:7])
        year = int(date[0:4])

        count = 0

        # 1, 3, 5, 7, 8, 10, 12 --> 31 days
        # 4, 6, 9, 11 --> 30 days
        # 2 then
        # have 29 (năm nhuận)
        for i in range(1, month):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                count += 31
            elif i == 2:
                if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
                    count += 29
                else:
                    count += 28
            else:
                count += 30
        
        return count + day