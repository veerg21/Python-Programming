print("Bubble Sort")
def bubble_sort(arr):
    print(arr, "is unsorted array")
    number=len(arr)
    # print(number)
    for i in range(number-1):
        for y in range(number-i-1):
            if arr[y]>arr[y+1]:
                arr[y], arr[y+1]=arr[y+1], arr[y]
ls=[8173, 53, 97134, 13724, 73819, 78324, 918734]
bubble_sort(ls)
print(ls, "is sorted array")