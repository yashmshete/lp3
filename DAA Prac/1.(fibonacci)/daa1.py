def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    n = int(input("Enter a positive integer to compute Fibonacci: "))
    print(f"Fibonacci (Iterative) of {n}: {fibonacci_iterative(n)}")
    print(f"Fibonacci (Recursive) of {n}: {fibonacci_recursive(n)}")
