'''
Time: O(n)
Space: O(n)
'''
from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums, k):
        if len(nums) < k:
            return sum(nums)
        i, j = 0, 0
        curr_sum, max_sum = 0, 0
        count = {}

        while j < len(nums):
            curr_sum += nums[j]
            # Check if nums[j] exists in count, if not initialize it
            if nums[j] in count:
                count[nums[j]] += 1
            else:
                count[nums[j]] = 1

            if j-i+1 > k:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    count.pop(nums[i])
                curr_sum -= nums[i] # Remove key if its value becomes 0
                i += 1

            if len(count) == k and j-i+1 == k:
                max_sum = max(max_sum, curr_sum)
            j += 1
        return max_sum
        
    def maximumSubarraySum1(self, nums, k):
        if len(nums) < k:
            return sum(nums)
        i, j = 0, 0
        curr_sum, max_sum = 0, 0
        count = defaultdict(int)

        while j < len(nums):
            curr_sum += nums[j]
            count[nums[j]] += 1

            if j-i+1 > k:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    count.pop(nums[i])
                curr_sum -= nums[i]
                i += 1
            if len(count) == k and j-i+1 == k:
                max_sum = max(max_sum, curr_sum)
            j += 1
        return max_sum


if __name__ == '__main__':
    soln = Solution()
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    print(soln.maximumSubarraySum1(nums, k))