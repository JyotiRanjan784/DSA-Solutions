class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        numbers = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):

                    if i == j or j == k or i == k:
                        continue

                    if digits[i] == 0:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    number = digits[i] * 100 + digits[j] * 10 + digits[k]

                    numbers.add(number)

        return len(numbers)