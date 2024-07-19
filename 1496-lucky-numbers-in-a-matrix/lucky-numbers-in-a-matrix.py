class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []

        row_min = set()
        for r in range(ROWS):
            row_min.add(min(matrix[r]))
        for c in range(COLS):
                cur_max = matrix[0][c]
                for r in range(ROWS):
                    cur_max = max(cur_max, matrix[r][c])
                if cur_max in row_min:
                    res.append(cur_max)
        
        return res