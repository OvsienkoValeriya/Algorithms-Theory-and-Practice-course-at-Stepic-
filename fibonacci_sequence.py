def fib(n):
    f = [i for i in range(0,41)]
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]
        

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
