import sys

def get_divisors(n):
    """Return a list of all positive divisors of n."""
    return [i for i in range(1, n + 1) if n % i == 0]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        result = get_divisors(n)
        print(result)
