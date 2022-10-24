class Solution:
    def maxLength(self, substrings: List[str]) -> int:

        combinations = set()
        for substring in substrings:
            letters = set(substring)
            if len(substring) != len(letters):
                continue
            for combination in list(combinations):
                if not set(combination).intersection(letters):
                    new_s = substring + combination
                    combinations.add(new_s)
            combinations.add(substring)
            
        return max([len(i) for i in combinations]) if combinations else 0