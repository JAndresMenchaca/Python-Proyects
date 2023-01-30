def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    for n in range(10):
        print(fibonacci(n))


if __name__ == "__main__":
    main()
