import math
import numpy as np

"""
Computes the maximum number of iterations required to reach the desired accuracy.
:param a: Start value.
:param b: End value.
:param err: Acceptable error tolerance.
:return: The maximum number of iterations.
"""


def max_steps(a, b, err):
    return int(np.floor(-np.log2(err / (b - a)) / np.log2(2) - 1))


"""
Performs the Bisection Method to find the root of a given function f within the interval [a, b].
:param f: Continuous function where f(a) and f(b) have opposite signs.
:param a: Start of the interval.
:param b: End of the interval.
:param tol: Tolerable error (default is 1e-6).
:return: The approximate root of f.
"""


def bisection_method(f, a, b, tol=1e-6):
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("The scalars a and b do not bound a root (f(a) and f(b) must have opposite signs)")

    steps = max_steps(a, b, tol)
    c, k = 0, 0

    # Logging for debugging
    print(f"{'Iteration':<10} {'a':<15} {'b':<15} {'f(a)':<15} {'f(b)':<15} {'c':<15} {'f(c)':<15}")

    while abs(b - a) > tol and k < steps:
        c = (a + b) / 2  # Midpoint calculation

        if f(c) == 0:
            return c  # Exact root found

        if f(c) * f(a) < 0:
            b = c  # Move left
        else:
            a = c  # Move right

        print(f"{k:<10} {a:<15.6f} {b:<15.6f} {f(a):<15.6f} {f(b):<15.6f} {c:<15.6f} {f(c):<15.6f}")
        k += 1

    return c  # Return the last computed root


"""
Main execution: Defines the function and runs the bisection method.
"""
if __name__ == '__main__':
    f = lambda x: (math.sin(x ** 2 + 5 * x + 6)) / (2 * math.exp(-x))

    # Interval range [-3,1]
    try:
        root = bisection_method(f, -3, 1)
        print(f"\nThe approximate root of f(x) is: {root}")
    except Exception as e:
        print(f"Error: {e}")