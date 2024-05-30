#!/usr/bin/python3
"""N queens"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

cols = set()
pos_diags = set()
neg_diags = set()

result = []
board = [[i, 0] for i in range(N)]


def backtrack(r):
    """a recursive function used for
    solving the n queens problem by backtracking"""
    if r == N:
        result.append([x[:] for x in board])
        return
    for c in range(N):
        if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
            continue
        cols.add(c)
        pos_diags.add(r + c)
        neg_diags.add(r - c)
        board[r][1] = c
        backtrack(r + 1)
        cols.remove(c)
        pos_diags.remove(r + c)
        neg_diags.remove(r - c)
        board[r][1] = 0


backtrack(0)
for solution in result:
    print(solution)
