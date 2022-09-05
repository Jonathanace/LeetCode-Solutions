class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        res = []
        for i in counts.most_common(k):
            res.append(i[0])
        return res