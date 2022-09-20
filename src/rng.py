def linear_congruent_generator(modulus: int,
                               multiplier: int,
                               increment: int,
                               seed: int) -> int:

    return (multiplier * seed + increment) % modulus


def lagged_fibonacci_generator(modulus: int,
                               first_dec: int,
                               second_dec: int,
                               seed: int) -> int:

    individuals = list(str(seed))
    seeds = [(individuals[first_dec - 1] * individuals[second_dec - 1]) % modulus for _ in range(len(individuals))]
    return int(''.join(seeds))
