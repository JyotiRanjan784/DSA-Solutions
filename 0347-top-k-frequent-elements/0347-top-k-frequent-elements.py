class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
        return sorted_nums[:k]