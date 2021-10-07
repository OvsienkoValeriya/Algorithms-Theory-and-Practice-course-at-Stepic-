#Дано целое число 1≤n≤10^3 и массив A[1…n] натуральных чисел, не превосходящих 2⋅10^9. Выведите #максимальное 1≤k≤n, для которого найдётся подпоследовательность 1≤i_1<i_2<…<i_k≤n длины k, в #которой каждый элемент делится на предыдущий (формально: для  всех 1≤j<k, A[i_j] ∣ A[i_j+1]).

def LisBottomUp(arr):  
    n = len(arr)
    d = [0 for i in range(n)] 
    d[0] = 1
    for i in range(1, n):
        d[i]=1
        for j in range(i):
            if arr[i]%arr[j] == 0 and d[j]+1>d[i]:   
                d[i]=d[j]+1
    ans = 0
    for i in range(n):
        ans = max(ans, d[i])
    return ans


def main():
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]  
    print(LisBottomUp(arr))

if __name__ == "__main__":
    main()
