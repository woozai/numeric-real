import numpy as np


def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Computes the root of f(x) using the Bisection Method.
    :param f: Function to find the root for.
    :param a: Left boundary of the interval.
    :param b: Right boundary of the interval.
    :param tol: Tolerance for the root.
    :param max_iter: Maximum number of iterations.
    :return: Approximate root of the function.
    """
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("The function must have opposite signs at a and b.")

    iterations = []
    for k in range(max_iter):
        c = (a + b) / 2  # Midpoint
        iterations.append((k, a, b, c, f(c)))

        if abs(f(c)) < tol or abs(b - a) < tol:
            return c, iterations

        if np.sign(f(c)) == np.sign(f(a)):
            a = c  # Move right
        else:
            b = c  # Move left

    return c, iterations  # Return last computed value


def find_valid_interval(f, start=-2, end=2, step=0.01):
    """Finds a valid interval where f(a) and f(b) have opposite signs."""
    x_vals = np.arange(start, end, step)
    for i in range(len(x_vals) - 1):
        if np.sign(f(x_vals[i])) != np.sign(f(x_vals[i + 1])):
            return x_vals[i], x_vals[i + 1]
    return None, None


if __name__ == "__main__":
    # Define function
    f = lambda x: np.sin(2 * np.exp(-2 * x)) / (2 * x ** 3 + 5 * x ** 2 - 6)

    # Define the interval within [-1, 1.2]
    a_new, b_new = find_valid_interval(f, -1, 1.2, 0.01)

    if a_new is not None and b_new is not None:
        print(f"נמצא טווח מתאים: a = {a_new}, b = {b_new}")
        root, iterations = bisection_method(f, a_new, b_new, 1e-6)
        print(f"\nApproximate largest root found in [-1,1.2]: x = {root}")
    else:
        print("לא נמצא טווח מתאים.")