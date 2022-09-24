def main():
    m = int(input("Enter first number: "))
    n = int(input("Enter second number: "))
    if are_permutation_of_same_digits(m, n):
        print(f"The numbers {m} and {n} are permutations of each other.")
    else:
        print(f"The numbers {m} and {n} are not permutations of each other.")


def are_permutation_of_same_digits(num1: int, num2: int) -> bool:
    """Returns True if num1 and num2 are permutations of each other, False otherwise."""

    return sorted_digits(num1) == sorted_digits(num2)


def sorted_digits(number: int) -> list:
    return sorted(str(number))


if __name__ == "__main__":
    main()
