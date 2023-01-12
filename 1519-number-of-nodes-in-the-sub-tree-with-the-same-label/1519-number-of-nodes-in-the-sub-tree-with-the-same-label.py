# source: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/discuss/3037908/Python-3-oror-11-lines-recursion-w-explanation-oror-TM%3A-100-95

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        
        for node_1, node_2 in edges:
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
            
        counts = defaultdict(int)
        res = [0] * n
        
        def dfs(node=0, parent=None):
            letter = labels[node]
            prev_count = counts[letter]
            counts[letter] += 1
            
            for child in graph[node]: 
                if child != parent:
                    dfs(child, node)
            
            res[node] = counts[letter] - prev_count
            
        dfs()
        return res