#Первая строка содержит число 1≤n≤10^4, вторая — n натуральных чисел, не превышающих 10. Выведите #упорядоченную по неубыванию последовательность этих чисел.

def countsort(input_arr):
    count_array = [0 for i in range(max(input_arr)+1)]
    for j in range(len(input_arr)):
        count_array[input_arr[j]] = count_array[input_arr[j]]+1       
    for i in range(1,len(count_array)):
        count_array[i] = count_array[i]+ count_array[i-1]  
    output_array = [0 for k in range(len(input_arr))]
    for j in range(len(input_arr)-1,-1, -1):   
        count_array[input_arr[j]] = count_array[input_arr[j]] - 1
        output_array[count_array[input_arr[j]]] = input_arr[j]
    
    return output_array

def main():
    int_count = int(input())
    arr = list(map(int,input().strip().split()))[:int_count]  
    print(*countsort(arr))

if __name__ == "__main__":
    main()
