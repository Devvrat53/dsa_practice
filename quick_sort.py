def quick_sort(arr, low, high):
    if low < high:
        position_pointer = partition(arr, low, high)
        quick_sort(arr, low, position_pointer-1)
        quick_sort(arr, position_pointer+1, high)

def partition(arr, low, high):
    i = low
    j = high - 1
    pivot = arr[high]

    while i < j:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 4, 6, 5]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)