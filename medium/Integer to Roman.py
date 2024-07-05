class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = []
        i = 0
        while num > 0:
            digits.append((num % 10)*(10**i))
            num //= 10
            i = i + 1
        digits.reverse()
        print(digits)

def tach_so(s):
    tien_te = [1000, 900, 90, 50, 5, 3]
    tien_te_str = ['1000', '900', '90', '50', '5', '3']
    result = []
    
    for i in range(len(tien_te)):
        count = s // tien_te[i]
        s -= count * tien_te[i]
        result.extend([tien_te_str[i]] * count)
        
    return result

so = int(input("Nhập một số bất kỳ: "))
ket_qua = tach_so(so)
print("Số {} được tách thành các mệnh giá: {}".format(so, ' + '.join(ket_qua)))



# a = Solution()
# c = int(input())
# a.intToRoman(c) # 1000 + 900 + 90 + 4
