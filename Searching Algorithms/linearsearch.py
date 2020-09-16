# Linear Search

def linearSearch(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i + 1
    else:
        return "Element not found"


if __name__ == "__main__":
    arr = [56, 78, 23, 18, 67]        # list to search 
    ele = 23                          # element to search in list
    result = linearSearch(arr, ele)
    print(result)