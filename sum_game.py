class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left = sum(int(c) for c in num[:mid] if c != '?')
        right = sum(int(c) for c in num[mid:] if c != '?')

        lq = num[:mid].count('?')
        rq = num[mid:].count('?')

        if (lq + rq) % 2:
            return True

        return left - right != 9 * (rq - lq) // 2