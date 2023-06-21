###
并不是拓扑排序
别看到课程表就拓扑

就是个bfs, 涉及到离线查询
花费额外空间记录即可


由于是个DAG, 那么边最多n - 1条, 即 O(n)
需要做n次bfs, 然后每次query花费 O(1) 时间
O(n*(n) + query)
O(n^2 + query)
###


import collections
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(list)
        for first, second in prerequisites:
            graph[first].append(second)
        first_to_second = defaultdict(set)
        
        for first in range(numCourses):
            self.bfs(first, graph, first_to_second)

        ans = []
        for first, second in queries:
            is_prerequisite = second in first_to_second[first]
            ans.append(is_prerequisite)
        return ans
    
    def bfs(self, start, graph, first_to_second):
        queue = collections.deque([start])
        vis = first_to_second[start]
        vis.add(start)

        while queue:
            curt = queue.popleft()
            for neighbor in graph[curt]:
                if neighbor in vis:
                    continue
                vis.add(neighbor)
                queue.append(neighbor)
        vis.remove(start)
