class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        for i in range(0, len(pos)):
            nums[2 * i] = pos[i]
            nums[(2 * i) + 1] = neg[i]
        return nums                        