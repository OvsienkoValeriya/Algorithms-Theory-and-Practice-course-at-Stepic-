#Первая строка содержит число 1≤n≤10^5, вторая — массив A[1…n], содержащий натуральные числа, не #превосходящие 10^9. Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j]. (Такая #пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором #смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет #вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)

inv_count = [0]

def sort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        sort1 = sort(arr[:m])
        sort2 = sort(arr[m:])
        return merge(sort1, sort2)
    else:
        return arr
    
def merge(arr1, arr2):
    sorted_arr = []
    i=0
    j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i]< arr2[j]:
            sorted_arr.append(arr1[i])
            i+=1
        elif arr1[i] == arr2[j]:
            sorted_arr.append(arr1[i])
            i+=1
            sorted_arr.append(arr2[j])
            inv_count[0]+=len(arr1) - i
            j+=1
        else:
            sorted_arr.append(arr2[j])
            inv_count[0]+=len(arr1)-i 
            j+=1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i+=1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j+=1

    return sorted_arr

def main():
    data = []
    for _ in range(2):
        data.append(list(map(int, input().split())))
    arr = data[1]
    sort(arr)
    print(inv_count[0])

if __name__ == "__main__":
    main()
