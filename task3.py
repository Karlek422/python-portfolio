def find_duplicates(my_list):
    duplicates = set()
    seen = set()
    for num in my_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
def find_duplicates(my_list):
    """
    Finds and returns a list of duplicate numbers in the input list.

    Args:
        my_list (list): The input list of numbers.

    Returns:
        list: A list of duplicate numbers found in the input list. Returns an empty list if no duplicates are found.

    Example:
        >>> find_duplicates([1, 2, 3, 4, 2, 3, 5])
        [2, 3]
    """
    duplicates = set()
    seen = set()
    for num in my_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)