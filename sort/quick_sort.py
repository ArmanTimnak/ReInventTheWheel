def quick_sort(arr):
    """
    Sorts a list in ascending order using the quicksort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.

    Example:
        >>> arr = [5, 2, 1, 3, 4]
        >>> quick_sort(arr)
        [1, 2, 3, 4, 5]
        >>> arr = [5, 1, 1, 3, 8, 6]
        >>> quick_sort(arr)
        [1, 1, 3, 5, 6, 8]
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)