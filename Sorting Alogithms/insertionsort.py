def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        # Moving elements greater than key to right side
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

if __name__ == "__main__":
    arr = [78, 56, 63, 18, 23]      # List to sort
    
    result = insertionSort(arr)
    print(result)