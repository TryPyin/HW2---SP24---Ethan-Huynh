import math

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Use the Secant Method to find the root of fcn(x) in the neighborhood of x0 and x1.

    Parameters:
    - fcn: the function for which we want to find the root
    - x0 and x1: two x values in the neighborhood of the root
    - xtol: exit if |xnewest - xprevious| < xtol
    - maxiter: exit if the number of iterations equals this number

    Returns:
    - The final estimate of the root (most recent new x value)
    """

    # Initialize variables
    x_prev = x0
    x_curr = x1

    # Perform iterations
    for i in range(maxiter):
        # Calculate the next approximation using the Secant method formula
        x_new = x_curr - fcn(x_curr) * (x_curr - x_prev) / (fcn(x_curr) - fcn(x_prev))

        # Check convergence
        if abs(x_new - x_curr) < xtol:
            return x_new

        # Update variables for the next iteration
        x_prev = x_curr
        x_curr = x_new

    return x_curr

def main():
    # Example 1
    x0, x1, maxiter, xtol = 1, 2, 5, 1e-4
    result1 = Secant(math.sin, x0, x1, maxiter, xtol)
    print(f"Solution 1: {result1}")

    # Example 2
    x0, x1, maxiter, xtol = 1, 2, 15, 1e-8
    result2 = Secant(math.sin, x0, x1, maxiter, xtol)
    print(f"Solution 2: {result2}")

    # Example 3
    x0, x1, maxiter, xtol = 1, 2, 3, 1e-8
    result3 = Secant(math.sin, x0, x1, maxiter, xtol)
    print(f"Solution 3: {result3}")

# Run the main function
main()
