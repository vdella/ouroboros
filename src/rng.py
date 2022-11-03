def linear_congruent_generator(modulus: int,
                               multiplier: int,
                               increment: int,
                               seed: int,
                               times: int = 1) -> int:
    result = list()

    for _ in range(times):
        result.append((multiplier * seed + increment) % modulus)

    return __to_int_from(result)


def blum_blum_shub_round1(seed, p, q, times=10):
    result = seed

    for _ in range(times):
        result = result**2 % (p*q)

    return result


def full_bbs(seed, times, p, q):
    result = [0 for _ in range(times)]

    for i in range(times):
        result[i] = blum_blum_shub_round1(seed, p, q)

    return __to_int_from(result)


def __to_int_from(values: list):
    middle = [str(value) for value in values]
    return int(''.join(middle))
