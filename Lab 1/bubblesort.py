def bubblesort(arr):
    a = len(arr)

    for i in range(a):
        for j in range(i + 1, a):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print(arr)


arr = [3, 2, 1, 4, -1]
bubblesort(arr)
