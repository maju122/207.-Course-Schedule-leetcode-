class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = done

        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            state[node] = 1
            for nxt in graph[node]:
                if has_cycle(nxt):
                    return True
            state[node] = 2
            return False

        return not any(has_cycle(i) for i in range(numCourses))
