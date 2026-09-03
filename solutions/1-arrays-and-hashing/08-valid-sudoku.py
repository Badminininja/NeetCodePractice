"""
LC 36 - Valid Sudoku

Determine if a 9x9 Sudoku board is valid: each row, each column, and each
of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.
Only filled cells need to be validated (board can be partially filled;
'.' represents an empty cell).

Approach:
    Rows, columns, and 3x3 squares are three INDEPENDENT "no duplicates"
    zones - a global "have I seen this digit anywhere" set would be wrong,
    since the same digit can validly appear in different rows/cols/squares.
    Track each zone's seen-digits with its own set, keyed by row index,
    column index, and (row // 3, col // 3) respectively. Single pass over
    all 81 cells.
"""


def isValidSudoku(board: list[list[str]]) -> bool:
    rows = {}      # rows[r] = set of digits seen in row r
    cols = {}      # cols[c] = set of digits seen in col c
    squares = {}   # squares[(r//3, c//3)] = set of digits seen in that box

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue

            if r not in rows:
                rows[r] = set()
            if c not in cols:
                cols[c] = set()
            square_key = (r // 3, c // 3)
            if square_key not in squares:
                squares[square_key] = set()

            if val in rows[r] or val in cols[c] or val in squares[square_key]:
                return False

            rows[r].add(val)
            cols[c].add(val)
            squares[square_key].add(val)

    return True


if __name__ == "__main__":
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]  # two 8's in column 0 (rows 0 and 3)

    assert isValidSudoku(valid_board) is True
    assert isValidSudoku(invalid_board) is False

    print("All tests passed.")
