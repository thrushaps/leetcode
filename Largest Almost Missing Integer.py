class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        n = len(nums)

        for i in range(n - k + 1):
          window = set(nums[i:i+k])
          for num in window:
            count[num] += 1

        result = -1
        for num in count:
            if count[num] == 1:
                result = max(result, num)

        return result  