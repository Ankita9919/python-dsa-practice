


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def main():
    n = int(input("Enter n: "))

    try:
        print("Fibonacci number:", fibonacci(n))
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
