class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dsum = 0
        prod = 1
        temp = n

        while temp > 0:
            digit = temp % 10
            dsum += digit
            prod *= digit
            temp //= 10 

        total = dsum + prod
        return n % total == 0