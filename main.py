from src.rng import linear_congruent_generator, full_bbs
from src.primality import is_prime, is_composite_for
from src.show import show
from time import time


size_in_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

table = list()


def rng_at(bit_size: int):
    start = time()
    result = linear_congruent_generator(2, 3, 4, 5, bit_size)
    end = time() - start
    table.append(['LCG - {} bits'.format(bit_size),
                  result,
                  end,
                  is_composite_for(263, result),
                  is_prime(263, result)])

    start = time()
    result = full_bbs(2, bit_size, 39, 61)
    end = time() - start
    table.append(['BBS - {} bits'.format(bit_size),
                  result,
                  end,
                  is_composite_for(263, result),
                  is_prime(263, result)])


if __name__ == '__main__':
    for size in size_in_bits:
        rng_at(size)

    show(table)
