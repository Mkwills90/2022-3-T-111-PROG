# radon hal Difficulty : 3.84,
# although keep in mind that two functions are given,
# list comprehension is the only challenge in this problem.

from math import sqrt


def main():
    a_list = get_list()
    print(prime_sum(a_list))


def get_list() -> list:
    """Gets numbers from user."""

    a_list = input("Enter elements of list seperated by commas: ").strip().split(",")
    a_list = [int(number) for number in a_list]
    return a_list


def prime_sum(the_given_list_of_numbers: list) -> int:
    """Returns the sum of all prime numbers from the list."""

    primes_only = [number for number in the_given_list_of_numbers if is_prime(number)]
    return sum(primes_only)


def is_prime(n: int) -> bool:
    """Returns True if the number n is prime, False otherwise."""

    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    main()
