class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for index, number in enumerate(nums): 
            if number in last_index and index - last_index[number] <= k:
                return True
            else:
                last_index[number] = index
                
        return False