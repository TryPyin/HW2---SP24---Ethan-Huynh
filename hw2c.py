def GaussSeidel(Aaug, x, Niter=15):
    """
    Use the Gauss-Seidel method to estimate the solution to a set of linear equations.

    Parameters:
    Aaug (list of lists): Augmented matrix [A | b] with N rows and N+1 columns.
    x (list): Initial guess vector.
    Niter (int): Number of iterations (default is 15).

    Returns:
    list: Final solution vector.
    """
    N = len(x)

    for k in range(Niter):
        for i in range(N):
            sigma = 0
            for j in range(N):
                if j != i:
                    sigma += Aaug[i][j] * x[j]

            x[i] = (Aaug[i][-1] - sigma) / Aaug[i][i]

    return x


def main():
    # System 1
    A1 = [[3, 1, -1], [1, 4, 1], [2, 1, 2]]
    b1 = [2, 12, 10]
    Aaug1 = [row + [b] for row, b in zip(A1, b1)]
    x1 = [0, 0, 0]

    solution1 = GaussSeidel(Aaug1, x1)
    print("Solution for System 1:", solution1)

    # System 2
    A2 = [[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]]
    b2 = [2, 12, 21, 37]
    Aaug2 = [row + [b] for row, b in zip(A2, b2)]
    x2 = [0, 0, 0, 0]

    solution2 = GaussSeidel(Aaug2, x2)
    print("Solution for System 2:", solution2)


if __name__ == "__main__":
    main()
