def bubbleSort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-1):
            # Comparing adjacent elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If element was not swapped it was at correct position
        # So, break the loop
        if not swapped:
            print('here', arr[i])
            break

    return arr

if __name__ == "__main__":
    # arr = [78, 56, 63, 18, 23]      # List to sort
    arr = [78, 18, 56, 23, 63]
    result = bubbleSort(arr)
    print(result)