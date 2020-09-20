def bubbleSort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-1):
            # Comparing adjacent elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # if the array is sorted
        if not swapped:
            break

    return arr

if __name__ == "__main__":
    arr = [78, 56, 63, 18, 23]      # List to sort
    
    result = bubbleSort(arr)
    print(result)