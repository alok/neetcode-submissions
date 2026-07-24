import itertools

# iters for rows cols
GOOD = set(str(i) for i in range(1, 10))


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(flat):
            # not full
            # mercifully don't have to check solvability (yet, though that could be fun but for another day and skill acqui)
            withoutdots = [f for f in flat if f != "."]
            nodupes = set(withoutdots)

            return GOOD.issuperset(nodupes) and len(nodupes)==len(withoutdots)

        def subgrid(topleft):
            r, c = topleft
            return [
                board[r + offr][c + offc] for offr, offc in itertools.product(range(3), repeat=2)
            ]

        # all 9 rows are each valid AND all 9 cols are each valid AND all 9 subgrids are valid
        # row iter
        rowsgood = all(valid(r) for r in board)
        boardT = list(zip(*board))  # iirc this swaps
        colsgood = all(valid(c) for c in boardT)
        corners = [(r, c) for r, c in itertools.product(range(0, 9, 3), repeat=2)]
        gridsgood = all(valid(subgrid(corner)) for corner in corners)
        return rowsgood and colsgood and gridsgood
        # subgrid_iter # i miss numpy
        # top corners: (0,0), (0,3), (0,6)
        # 3,3 ..
        # 9 corners of form (3i,3j) for i j in range(3)
        # slice given a corner: r+offx,c+offy for offset in range(3)