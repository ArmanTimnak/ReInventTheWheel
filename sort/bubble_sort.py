def bubble_sort(arr):
    """
    Sorts the given list in ascending order using the bubble sort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    None. The original list is sorted in-place.

    Example:
        >>> arr = [5, 2, 1, 3, 4]
        >>> bubble_sort(arr)
        >>> arr
        [1, 2, 3, 4, 5]
    """
    n = len(arr)
     
    for i in range(n):
        swapped = False
 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break