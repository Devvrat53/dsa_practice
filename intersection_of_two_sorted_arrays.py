class Solution():
    def intersect_arrays(self, arr1, arr2):
        i, j = 0, 0
        intersect_arr = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                intersect_arr.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        return intersect_arr

if __name__ == '__main__':
    soln = Solution()
    arr1 = [1, 1, 2, 2, 3, 4, 5]
    arr2 = [1, 1, 3, 5, 6, 7]
    print(soln.intersect_arrays(arr1, arr2))