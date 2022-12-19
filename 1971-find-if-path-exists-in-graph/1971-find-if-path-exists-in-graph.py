class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ds = [-1] * n
        def find(i):
            if ds[i] == -1:
                return i
            else:
                return find(ds[i])
            
        for node1, node2 in edges:
            parent_1 = find(node1)
            parent_2 = find(node2)
            if parent_1 != parent_2:
                ds[parent_2] = parent_1
                
        return find(source) == find(destination)