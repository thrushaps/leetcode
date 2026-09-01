class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []

        for n in nums1:
            for i in range(len(nums2)):
                if nums2[i] == n:
                    for x in nums2[i + 1:]:
                        if x > n:
                            result.append(x)
                            break
                    else:
                        result.append(-1)
                    break

        return result