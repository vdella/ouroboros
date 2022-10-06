from math import log2


def is_composite_for(entry, random_num) -> bool:
    """Uses Miller-Rabin algorithm to check for possible primality."""

    odd_part, even_part = repart(entry - 1)  # Assuming 'number - 1' to be an even number.
    base = random_num
    probably_prime = (base**odd_part) % entry

    if probably_prime % entry == 1 % entry:
        return False

    for _ in range(even_part):
        if probably_prime % entry == -1 % entry:
            return False
        probably_prime = probably_prime ** 2 % entry

    return True


def is_prime(entry, random_num) -> bool:
    """Uses Fermat's primality test to check if a number is prime or composite."""
    for _ in range(8):
        base = random_num

        if (base**(entry - 1)) % entry != 1 % entry:
            return False

    return True


def repart(even_number) -> tuple:
    """Digests an even number into its odd and even parts as 2^k * m."""

    odd_part = even_number

    while odd_part % 2 == 0:
        odd_part //= 2  # Divides by 2 as much as possible to get its odd part.

    even_part = log2(even_number / odd_part)  # Gets even part k by solving 2^k * m.

    return odd_part, int(even_part)
