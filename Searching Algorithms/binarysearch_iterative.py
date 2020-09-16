# Binary Search - Iterative

def binarySearch(arr, ele):
    size = len(arr)
    low = 0
    high = len(arr) - 1

    while high >= low:
        # Finding mid point
        mid = low + (high - low)//2

        # if element is present at middle
        if arr[mid] == ele:
            return mid + 1
        
        # if element is smaller than mid, move to left subarray
        elif arr[mid] > ele:
            high = mid - 1

        # if element is greater than mid, move to right subarray
        else:
            low = mid + 1

    return -1
 
if __name__ == "__main__":
    arr = [18, 23, 56, 67, 78]        # Binary search takes a sorted list 
    ele = 78                          # element to search in list
    low = 0
    high = len(arr) - 1 
    
    result = binarySearch(arr, ele)
    if result != -1:
        print(f"Position of element is {result}")
    else:
        print("Element not in list")