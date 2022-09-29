def find_index_of_nth_occurrence(sequence, element_to_find, occurrence):
    """Returns the location of the n-th occurrence of an element within a sequence."""

    seen_so_far = 0
    for index, element in enumerate(sequence):
        if element == element_to_find:
            seen_so_far += 1
            if seen_so_far == occurrence:
                return index
    return -1
