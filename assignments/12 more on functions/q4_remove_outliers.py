from copy import deepcopy


def main():
    a_list = [3, 9, 5, 1, 6, 8]
    print(f"Before calling remove_min_and_max: {a_list = }")
    remove_min_and_max(a_list)
    print(f"After calling remove_min_and_max: {a_list = }")

    b_list = [9, 2, 3, 6, 1, 8, 7]
    print(f"Before calling without_outliers: {b_list = }")
    c_list = without_outliers(b_list)
    print(f"After calling without_outliers: {b_list = }")
    print(f"After calling without_outliers: {c_list = }")


def remove_min_and_max(a_list: list) -> None:
    """Removes the lowest number and the highest number from the list."""

    a_list.remove(min(a_list))
    a_list.remove(max(a_list))


""" 
# Alternatively:
def remove_min_and_max(a_list: list) -> None:    
    min_index, max_index = find_min_and_max_index(a_list)

    a_list.pop(min_index)

    if min_index < max_index:
        max_index -= 1

    a_list.pop(max_index)
 """


def without_outliers(a: list) -> list:
    """Returns a copy of the given list, with the lowest and highest numbers excluded."""

    min_index, max_index = find_min_and_max_index(a)
    return [a[i] for i in range(len(a)) if (i != min_index and i != max_index)]


""" 
# Alternatively:
def without_outliers(a_list:list) -> list:
    new_list = deepcopy(a_list)
    remove_min_and_max(new_list)
    return new_list
 """


def find_min_and_max_index(a_list: list) -> tuple:
    """Finds the position of the lowest number and the highest number in the list."""

    min_index = a_list.index(min(a_list))
    max_index = a_list.index(max(a_list))
    return min_index, max_index


""" 
# Alternatively:
def find_min_and_max_index(a_list: list) -> tuple:
    min_index, max_index = 0, 0

    for i in range(1, len(a_list)):
        if a_list[i] < a_list[min_index]:
            min_index = i

        if a_list[i] > a_list[max_index]:
            max_index = i

    return min_index, max_index
 """


if __name__ == "__main__":
    main()
