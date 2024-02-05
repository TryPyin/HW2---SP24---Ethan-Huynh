import math

def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability using Simpson's 1/3 rule for integration.

    Parameters:
    - PDF (function): Callback function for the Gaussian/normal probability density function.
    - args (tuple): Tuple containing μ and σ.
    - c (float): Upper limit of integration.
    - GT (bool): Boolean indicating if we want the probability of x being greater than c (GT=True) or less than c (GT=False).

    Returns:
    - float: Probability value.
    """
    mu, sigma = args

    # Define the integration limits
    x_lower = mu - 5 * sigma
    x_upper = c

    # Number of intervals for Simpson's rule (adjust for accuracy)
    n_intervals = 1000

    # Calculate the width of each interval
    delta_x = (x_upper - x_lower) / n_intervals

    # Initialize the result of integration
    result = 0.0

    # Apply Simpson's 1/3 rule
    for i in range(n_intervals + 1):
        x = x_lower + i * delta_x
        weight = 4 if i % 2 == 1 else 2  # 4 for odd index, 2 for even index
        result += weight * PDF((x, mu, sigma))

    result *= delta_x / 3

    # Return the probability based on GT
    return result if GT else 1 - result


def normal_pdf(data):
    """
    Gaussian/normal probability density function callback.

    Parameters:
    - data (tuple): Tuple containing x, μ (population mean), and σ (population standard deviation).

    Returns:
    - float: Probability density function value.
    """
    x, mu, sigma = data
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(exponent)


def main():
    # Example 1: P(x<105|N(100,12.5))
    result1 = Probability(normal_pdf, (100, 12.5), 105, GT=True)
    print(f'P(x<105|N(100,12.5))={result1:.2f}')

    # Example 2: P(x>μ+2σ|N(100,3))
    result2 = Probability(normal_pdf, (100, 3), 100 + 2 * 3, GT=False)
    print(f'P(x>{100 + 2 * 3}|N(100,3))={result2:.2f}')


if __name__ == "__main__":
    main()
