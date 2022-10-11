class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest_num = float('inf')
        second_low = float('inf')
        for num in nums:
            if num < lowest_num:
                lowest_num = num
            elif lowest_num < num < second_low:
                second_low = num
            elif num > second_low: 
                return True
        return False