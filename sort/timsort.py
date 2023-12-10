def insertion_sort(arr, left=0, right=None):
    """
    Sorts the given array using the insertion sort algorithm.

    Parameters:
    arr (list): The array to be sorted.
    left (int): The starting index of the subarray to be sorted (default is 0).
    right (int): The ending index of the subarray to be sorted (default is None, which means the entire array).

    Returns:
    list: The sorted array.
    """

    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1

        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key_item

    return arr

def timsort(arr):
    """
    Sorts the given array using the Timsort algorithm.

    Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort.
    It is designed to perform well on many kinds of real-world data.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.

    Example:
        >>> arr = [5, 2, 1, 3, 4]
        >>> timsort(arr)
        [1, 2, 3, 4, 5]
    """
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            merged_arr = merge(
                left=arr[start:midpoint + 1],
                right=arr[midpoint + 1:end + 1])

            arr[start:start + len(merged_arr)] = merged_arr

        size *= 2

    return arr