#!/usr/bin/env python
# encoding: utf-8

class PriorityQueue:

    def __init__(self, items=[]):
        self.elements = []
        for item in items:
            heap.heappush(self.elements, (0, item))

    def __len__(self):
        return len(self.elements)

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def a_star_search(start, goal, successor, heuristic):
            frontier = PriorityQueue()
            frontier.put(start, 0)
            visited = set()
            came_from = dict()
            cost_so_far = {start: 0}

            while frontier:
                node = frontier.get()
                if node in visited:
                    continue
                if goal(grid, node):
                    return reconstruct_path(came_from, start, node)
                visited.add(node)

                for item in successor(grid, node):
                    frontier.put(
                        item,
                        priority = cost_so_far[node] + 1 + heuristic(grid, item)
                    )
                    if item not in cost_so_far or cost_so_far[node] + 1 < cost_so_far[item]:
                        cost_so_far[item] = cost_so_far[node] + 1
                        came_from[item] = node
            return None

        def reconstruct_path(came_from, start, end):
            reverse_path = [end]
            while end != start:
                end = came_from[end]
                reverse_path.append(end)
            return list(reversed(reverse_path))

        def get_successor(grid, cell):
            i, j = cell
            res = []
            for x, y in [(i + 1, j + 1),
                    (i + 1, j    ),
                    (i + 1, j - 1),
                    (i    , j + 1),
                    (i    , j - 1),
                    (i - 1, j + 1),
                    (i - 1, j    ),
                    (i - 1, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                    res.append((x,y))
            return res

        def get_heuristic(grid, cell):
            M, N = len(grid), len(grid[0])
            return max(abs(M - 1 - cell[0]), abs(N - 1 - cell[1]))


        def get_goal(grid, cell):
            M, N = len(grid), len(grid[0])
            return cell == (M - 1, N - 1)

        shortest_path = a_star_search(
            start = (0, 0),
            goal = get_goal,
            successor = get_successor,
            heuristic = get_heuristic
        )

        if shortest_path is None or grid[0][0] == 1:
            return -1
        else:
            return len(shortest_path)

