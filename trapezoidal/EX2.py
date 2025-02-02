import math


def trapezoidal_rule(f, a, b, n):
    """
    Trapezoidal Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals.

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h
    return integral


if __name__ == "__main__":
    # Define the function from the image
    def f(x):
        return (x * math.exp(-x ** 2 + 5 * x)) * (2 * x ** 2 - 3 * x - 5)


    # Define integration parameters
    a, b = 0.5, 1  # Integration limits
    n = 10  # Number of subintervals

    result = trapezoidal_rule(f, a, b, n)
    print("Approximate integral:", result)
