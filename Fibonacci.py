def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci series up to {num_terms} terms:")
print(fibonacci(num_terms))
