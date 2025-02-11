# https://leetcode.com/problems/trapping-rain-water/description/ 
class Solution:
    # Using  prefix max and suffix max approach (Dynamic Programming)
    def trap1(self, height) -> int:
        if not height:
            return 0
        left = [height[0]]
        right = [height[-1]]
        for i in range(1, len(height)):
            left.append(max(left[-1], height[i]))
        for j in range(len(height)-2, -1, -1): # range(start, end, step)
            right.append(max(right[-1], height[j]))
        right.reverse()
        trapped_water = 0
        for i in range(len(height)):
            trapped_water += min(left[i], right[i]) - height[i]
        return trapped_water

    # Using Two Pointer approach 
    def trap2(self, height) -> int:
        left_max, right_max = 0, 0
        left, right = 1, len(height)-2
        trapped_water = 0
        while left <= right:
            left_max = max(left_max, height[left-1])
            right_max = max(right_max, height[right+1])
            if left_max <= right_max:
                if left_max > height[left]:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if right_max > height[right]:
                    trapped_water += right_max - height[right]
                right -= 1
        return trapped_water

if __name__ == '__main__':
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap1(height))
    print(solution.trap2(height))
