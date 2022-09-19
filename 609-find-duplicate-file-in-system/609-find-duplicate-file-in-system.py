class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for path in paths:
            directory = path.split(' ')[0]
            for file in path.split(' ')[1:]:
                contents = file[file.index('(')+1:file.index(')')]
                d[contents].append(directory + '/' + file[:file.index('(')])
            # print()
                        
        res = []
        for value in d.values():
            if len(value) > 1:
                res.append(value)
                
        return res