
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        row = 0
        direction = 1  # 1 = down, -1 = up

        for ch in s:
            rows[row] += ch

            # Change direction at the top and bottom
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(rows)

