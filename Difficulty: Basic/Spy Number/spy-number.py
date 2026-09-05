class Solution:
    def checkSpy(self, n):
        # code here
        number = str(n)
        sum1 = 0
        prod = 1

        for digit in number:
            d = int(digit)
            sum1 += d
            prod *= d

        return sum1 == prod