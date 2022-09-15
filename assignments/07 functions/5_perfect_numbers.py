def sum_of_factors(number):
    sum_of_factors = 0
    for potential_factor in range(1, number // 2 + 1):  # No need to look any further.
        if number % potential_factor == 0:
            # Potential factor becomes an actual factor
            sum_of_factors += potential_factor
    return sum_of_factors


def decide(number):
    sum_of_its_factors = sum_of_factors(number)

    if sum_of_its_factors > number:
        return f"{number} is abundant."
    elif sum_of_its_factors < number:
        return f"{number} is deficient."
    else:
        return f"{number} is a perfect number."
