from rng import linear_congruent_generator
from math import log2


def is_composite_for(*args) -> bool:
    """Uses Miller-Rabin algorithm to check for possible primality."""

    number = args[0]
    rng = args[1]
    foo, bar, seed = args[2:]

    odd_part, even_part = repart(number - 1)  # Assuming 'number - 1' to be an even number.

    base = rng(number, foo, bar, seed)

    probably_prime = (base**odd_part) % number

    if probably_prime % number == 1 % number:
        return False

    for _ in range(int(even_part)):
        if probably_prime % number == -1 % number:
            return False
        probably_prime = probably_prime**2 % number

    return True


def is_prime(*args) -> bool:
    """Uses Fermat's primality test to check if a number is prime or composite."""

    number = args[0]
    rng = args[1]
    foo, bar, seed = args[2:]

    for _ in range(8):
        base = rng(number, foo, bar, seed)

        if (base**(number - 1)) % number != 1 % number:
            return False

    return True


def repart(even_number) -> tuple:
    """Digests an even number into its odd and even parts as 2^k * m."""

    odd_part = even_number

    while odd_part % 2 == 0:
        odd_part //= 2  # Divides by 2 as much as possible to get its odd part.

    even_part = log2(even_number / odd_part)  # Gets even part k by solving 2^k * m.

    return odd_part, int(even_part)


if __name__ == '__main__':
    print(is_composite_for(261, linear_congruent_generator, 3, 4, 5))
    print(is_prime(261, linear_congruent_generator, 3, 4, 5))
