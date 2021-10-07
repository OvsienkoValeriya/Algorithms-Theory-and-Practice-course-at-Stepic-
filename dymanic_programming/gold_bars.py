#Первая строка входа содержит целые числа 1≤W≤10^4 и 1≤n≤300 — вместимость рюкзака и число золотых #слитков. Следующая строка содержит n целых чисел 0≤w_1,…,w_n≤10^5, задающих веса слитков. Найдите #максимальный вес золота, который можно унести в рюкзаке.

def knapsack(W, weights):
    arr = [1] + [0] * W
    arr_new = arr[:]
    for i in range(len(weights)):
        for j in range(weights[i], W+1):
            if arr[j - weights[i]] == 1:
                arr_new[j] = 1
        arr = arr_new[:]  
        
    for i in range(W, -1, -1):
        if arr[i] == 1:
            return i
    return 0
        
def main():
        W, count = map(int, input().split())
        weights = list(map(int,input().split()))
        print(knapsack(W, weights))
    
if __name__ == "__main__":
    main()
