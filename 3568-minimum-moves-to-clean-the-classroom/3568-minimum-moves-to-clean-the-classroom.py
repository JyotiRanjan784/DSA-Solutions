from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find S and number every L
        litter = {}
        start = None

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)
        all_mask = (1 << k) - 1

        # BFS: (row, col, mask, remaining_energy, moves)
        q = deque()
        sr, sc = start

        q.append((sr, sc, 0, energy, 0))

        # For each (r, c, mask), store the maximum energy seen
        visited = {}
        visited[(sr, sc, 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, curr_energy, moves = q.popleft()

            # All litter collected
            if mask == all_mask:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid or obstacle
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                # Cannot move without energy
                if curr_energy == 0:
                    continue

                new_energy = curr_energy - 1
                new_mask = mask

                # Collect litter
                if (nr, nc) in litter:
                    i = litter[(nr, nc)]
                    new_mask |= (1 << i)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (nr, nc, new_mask)

                # Already reached this state with more energy
                if state in visited and visited[state] >= new_energy:
                    continue

                visited[state] = new_energy

                q.append(
                    (nr, nc, new_mask, new_energy, moves + 1)
                )

        return -1