'''
Sliding Window
'''
class Solution():
    def longestuniquesubstring(self, s):
        if len(s) <= 1:
            return len(s)
        i, j = 0, 0
        max_length = 0
        start = 0
        sett = set()

        while j < len(s):
            while s[j] in sett: # when duplicate element is found and window is invalid remove from set
                sett.remove(s[i]) 
                i += 1
            sett.add(s[j])
            if (max_length < j-i+1): # j-i+1 = size of the window
                start = i
                max_length = j-i+1
            j += 1
        #return s[start:start+max_length]
        return max_length, s[start:start+max_length]

if __name__ == '__main__':
    s = 'pwwkew'
    soln = Solution()
    max_length, substring = soln.longestuniquesubstring(s)
    print(f"Substring {substring} is the longest substring of length {max_length}")