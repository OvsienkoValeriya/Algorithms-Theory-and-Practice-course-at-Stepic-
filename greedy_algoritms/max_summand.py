#По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно представить как #сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k #слагаемых.

def max_summand(n):
    summands = []  
    for k in range(1, n+1):    
        n-=k 
        if n>k:
            summands.append(k)      
        elif n >= 0: 
            summands.append(k+n)
        else:
            break
    print(len(summands))
    print(*summands)

def main():
    n = int(input())
    max_summand(n)


if __name__ == "__main__":
    main()

