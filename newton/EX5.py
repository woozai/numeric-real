import math

class bcolors:
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'

def newton_raphson(f, df, p0, TOL, N=50):
    print("{:<10} {:<15} {:<15} ".format("Iteration", "po", "p1"))
    for i in range(N):
        if df(p0) == 0:
            print("Derivative is zero at p0, method cannot continue.")
            return None

        p = p0 - f(p0) / df(p0)

        if abs(p - p0) < TOL:
            return p
        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p))
        p0 = p

    return p

if __name__ == '__main__':
    # Define the function and its derivative
    f = lambda x: (math.sin(x**2 + 5*x + 6)) / (2 * math.exp(-x))
    df = lambda x: (math.exp(x) * math.sin(x**2 + 5*x + 6) / 2) + ((2*x + 5) * math.exp(x) * math.cos(x**2 + 5*x + 6) / 2)

    # List of initial guesses
    initial_guesses = [-3, -2.9, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1]
    tolerance = 1e-6
    max_iterations = 50

    # Iterate over initial guesses
    for initial_guess in initial_guesses:
        print(f"\nStarting Newton-Raphson with initial guess: {initial_guess}")
        approximate_root = newton_raphson(f, df, initial_guess, tolerance, max_iterations)

        # Check if a root was found and print the result
        if approximate_root is not None:
            print(bcolors.OKBLUE +
                  "\nThe equation f(x) has an approximate root at x = {:<15.9f}".format(approximate_root) +
                  bcolors.ENDC)
        else:
            print("The method did not converge to a root.")
