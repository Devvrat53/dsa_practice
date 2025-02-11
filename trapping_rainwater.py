# https://leetcode.com/problems/trapping-rain-water/description/ 
class Solution:
    def trap(self, height) -> int:
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

if __name__ == '__main__':
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap(height))
