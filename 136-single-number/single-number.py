class Solution(object):
    def singleNumber(self, nums):
        unique_number = 0
        for num in nums:
            unique_number ^= num
        return unique_number