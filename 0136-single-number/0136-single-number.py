class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res=0
        for i in nums:
            res=res^i
        return res