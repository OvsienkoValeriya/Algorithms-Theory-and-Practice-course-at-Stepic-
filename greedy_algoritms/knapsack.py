#Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6. Каждая из #следующих n строк задаёт стоимость 0≤c_i≤2⋅10^6 и объём 0<w_i_≤2⋅10^6 предмета (n, W, c_i w_i ​ — #целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно #отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в #данный рюкзак, с точностью не менее трёх знаков после запятой.

def knapsack(things_count, sack_volume, 
             tuple_list):  
    result_price = 0
    for i in sorted(tuple_list, key=lambda x:x[0]/x[1], reverse=True):
        if i[1] < sack_volume:
            result_price += i[0]
            sack_volume = sack_volume - i[1]
        else:
            result_price += sack_volume*(i[0]/i[1])
            break 
    print(format(result_price, '.3f'))

def main():
    things_count, sack_volume = map(int, input().split())
    tuple_list = []
    for thing in range(things_count):
        (price, volume) = map(int, input().split())
        tuple_list.append((price, volume))
    knapsack(things_count, sack_volume, tuple_list)

if __name__ == "__main__":
    main()

