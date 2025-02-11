class Solution:
    # Method 1
    def removeDuplicates1(self, nums) -> int:
        if len(nums) <= 1: # length of array less than or equal to 1
            return 1
        i, j = 1, 1
        while j < len(nums): # loop through the array
            while j < len(nums) and nums[i-1] == nums[j]: 
                j += 1
                if j == len(nums): # if there is a small array [1, 1], and j = len(nums)
                    break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        return i
    
    # Method 2: Efficient method
    def removeDuplicates2(self, nums) -> int:
        if len(nums) <= 1:
            return 1
        i, j = 0, 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            elif nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1
    
    # Method 3: More clean
    def removeDuplicates3(self, nums) -> int:
        if len(nums) <= 1: # length of array less than or equal to 1
            return 1
        i, j = 1, 1
        while j < len(nums): # loop through the array
            if nums[i-1] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i
    
if __name__ == '__main__':
    solution = Solution()
    arr = [0,0,1,1,1,2,2,3,3,4]
    # print(solution.removeDuplicates1(arr))
    # print(solution.removeDuplicates2(arr))
    print(solution.removeDuplicates3(arr))
