'''
Reference: https://www.youtube.com/watch?v=XiuSW_mEn7g&ab_channel=CSDojo
Time complexity: O(d(n+k)) 
                where d is the digits 
                      k is the base 10
                      n is the length of the array
'''
def get_max(arr):
    return max(arr)

def radix_sort(arr):
    max_num = get_max(arr)
    exp = 1
    while max_num // exp > 0:
        # Grouping the digits
        bucket = [[] for _ in range(10)]
        #print(bucket)
        
        # Flattening the buckets
        for num in arr:
            index = (num // exp) % 10
            bucket[index].append(num)
            #print(bucket)
        
        arr.clear()
        for sublist in bucket:
            arr.extend(sublist)
            #print(arr)
        
        exp *= 10

if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)
    print(arr)