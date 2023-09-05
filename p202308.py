import math
from typing import Tuple


class P202308Solver:
    def solve(self) -> Tuple[float, float]:
        term_sqrt = math.sqrt(256 - 54 * math.pi)
        P_max = (16 - term_sqrt) * (4 * term_sqrt + 27 * math.pi - 64) / (243 * math.pi)
        D_opt = (16 - term_sqrt) / 9
        return D_opt, P_max


if __name__ == '__main__':
    p202308_solver = P202308Solver()
    print(p202308_solver.solve())
