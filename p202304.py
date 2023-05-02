import math
from functools import cache


class P202304Solver:
    def solve(self) -> float:
        @cache
        def c(n: int, m: int) -> int:
            if n == m or m == 0:
                return 1
            return c(n - 1, m - 1) + c(n - 1, m)
        t_1 = c(20, 10) * 8 + c(18, 9)
        t_2 = c(22, 11) * 7 + c(20, 10) * 2
        t_3 = c(22, 11) * 6 + c(20, 10) * 3
        edge_pairs = t_1 * 2 + t_2 * 4 + t_3 * 4 >> 1
        i_1, i_2, i_3 = c(22, 11), c(24, 12), c(24, 12)
        adj_pairs = i_1 * 2 + i_2 * 4 + i_3 * 4
        return edge_pairs + adj_pairs << 1


if __name__ == '__main__':
    p202304_solver = P202304Solver()
    print(round(p202304_solver.solve()))
