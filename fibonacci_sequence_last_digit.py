def fib_digit(n):
    a, b = 1, 1
    for i in range(2,n+1):
        t=(a+b)%10
        a = b
        b = t
    return a


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
