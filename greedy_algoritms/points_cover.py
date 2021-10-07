#По данным n n n отрезкам необходимо найти множество точек минимального размера, для которого #каждый из отрезков содержит хотя бы одну из точек.

#В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа #0≤l≤r≤10^9, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. #Если таких множеств точек несколько, выведите любое из них.

def PointsCover(intervals_count, tuple_list):

    points = []
    sorted_list = list(sorted(tuple_list, key=lambda x:x[1]))
    first = sorted_list[0]
    points.append(first[1])
    for i in range(1, len(sorted_list)):
        interval = sorted_list[i]
        prev = points[-1]   
        if interval[1]>=prev and interval[0]<= prev:
            continue
        else:
            points.append(interval[1])
    
    print(len(points))
    print(*points)

def main():

    intervals_count = int(input())
    tuple_list = []
    for interval in range(intervals_count):
        (start, end) = map(int, input().split())
        tuple_list.append((start, end))
    PointsCover(intervals_count, tuple_list)


if __name__ == "__main__":
    main()
