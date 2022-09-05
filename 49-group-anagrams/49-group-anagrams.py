class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            d[''.join(sorted(list(word)))].append(word)
        res = []
        for key in d.keys():
            res.append(d[key])
        return res