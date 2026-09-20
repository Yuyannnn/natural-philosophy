#!/usr/bin/env python3
"""Check the change-of-basis example in math/linear-maps-and-matrices.md.

Column-vector convention: x = P z, so the new matrix is P^-1 A P.
Fraction arithmetic keeps this small rational example exact.
"""
from fractions import Fraction
from itertools import product


def matmul(left, right):
    """Multiply two matrices; this example uses only 2-by-2 matrices."""
    return tuple(
        tuple(sum(a * b for a, b in zip(row, column)) for column in zip(*right))
        for row in left
    )


def matvec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def main():
    a = ((2, 1), (1, 2))
    p = ((1, 1), (1, -1))
    half = Fraction(1, 2)
    p_inverse = ((half, half), (half, -half))
    identity = ((1, 0), (0, 1))
    assert matmul(p_inverse, p) == matmul(p, p_inverse) == identity

    transformed = matmul(matmul(p_inverse, a), p)
    assert transformed == ((3, 0), (0, 1))
    # The matrix identity checks all vectors; this grid illustrates both routes.
    assert matmul(a, p) == matmul(p, transformed)
    for coordinates in product(range(-3, 4), repeat=2):
        assert matvec(a, matvec(p, coordinates)) == matvec(p, matvec(transformed, coordinates))

    x = (2, 0)
    z = matvec(p_inverse, x)
    result = matvec(p, matvec(transformed, z))
    assert z == (1, 1) and result == matvec(a, x) == (4, 2)
    print("P^-1 A P = diag(3, 1)")
    print("x = (2, 0) -> z = (1, 1) -> z' = (3, 1) -> x' = (4, 2)")
    print("PASS: exact matrix identity and both coordinate routes agree.")


if __name__ == "__main__":
    main()
