class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            d[''.join(sorted(list(i)))].append(i)
            
        return [i for i in d.values()]