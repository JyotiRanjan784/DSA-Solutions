class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        start = 1000
        commas = 1

        while start <= n:
            end = start * 1000 - 1
            if n < end:
                end = n
            count = end - start + 1
            total += count * commas
            start *= 1000
            commas += 1
        return total