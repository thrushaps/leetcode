from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = defaultdict(set)

        
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                rows[r].add(c)

        total = 0

        
        for r in rows:
            seats = rows[r]

            left = all(x not in seats for x in [2,3,4,5])
            right = all(x not in seats for x in [6,7,8,9])
            middle = all(x not in seats for x in [4,5,6,7])

            if left and right:
                total += 2
            elif left or right or middle:
                total += 1

        
        total += (n - len(rows)) * 2

        return total