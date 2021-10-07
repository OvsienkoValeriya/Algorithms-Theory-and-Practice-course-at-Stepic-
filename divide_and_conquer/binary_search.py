#В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел, не #превышающих 10^9, в порядке возрастания, во второй — целое число 1≤k≤10^5 и k натуральных чисел #b_1,…,b_k​, не превышающих 10^9. Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для #которого A[j]=b_i​, или −1 , если такого j нет.

def binary_search(elem_list, start, end, key):
    if end >= start:
        mid_index = start + (end - start) // 2
        if elem_list[mid_index] == key:
            return mid_index
        elif elem_list[mid_index] > key:
            return binary_search(elem_list, start, mid_index-1, key)
        else:
            return binary_search(elem_list, mid_index+1, end, key)
    else:
        return -1

def main():  
    data = []
    for _ in range(2):
        data.append(list(map(int, input().split())))
  
    lst1 = data[0]
    lst1.pop(0)
  
    lst2 = data[1]
    k = lst2[0]
    lst2.pop(0)
    keys_str = []
    for i in range(0,k):
        ind = binary_search(lst1, 0, len(lst1)-1, lst2[i])
        if ind >= 0:
            keys_str.append(ind+1)
        else:
            keys_str.append(ind)


    print(*keys_str)

if __name__ == "__main__":
    main()
