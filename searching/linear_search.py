print("This is a linear search project")
def linearSearch(arr, num):
    #print("fun", arr, num)
    for y in range(8):
        #  
        if num==arr[y]:
            # print("found")
            return y
    
    return -1
# linearSearch()
ls=[21, 45, 43, 57, 2, 34, 765, 323]
x=int(input("Enter the number you want to search: "))
result=linearSearch(ls, x)
if result == -1:
    print("not found")
else:
    print("found, index number is ", result )