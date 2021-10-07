#В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на #прямой, соответственно. Следующие n строк содержат по два целых числа a_i и b_i (a_i≤b_i​) — #координаты концов отрезков. Последняя строка содержит m целых чисел — координаты точек. Все #координаты не превышают 10^8 по модулю. Точка считается принадлежащей отрезку, если она находится #внутри него или на границе. Для каждой точки в порядке появления во вводе выведите, скольким #отрезкам она принадлежит.

def binary_search(arr, start, end, key, strongly_less = False):
    n = 0
    while (start <= end):
        mid_ind = (start + end) // 2
        if strongly_less:
            if arr[mid_ind] < key:
                n = mid_ind + 1
                start = mid_ind + 1
            else:
                end = mid_ind - 1
        else:
            if arr[mid_ind] <= key:
                n = mid_ind + 1
                start = mid_ind + 1
            else:
                end = mid_ind - 1
     
    return n


def main():
    intervals_count, dots_count = map(int, input().split())
    intervals_start = []
    intervals_end = []
    for i in range(intervals_count):
        start, end = map(int, input().split())
        intervals_start.append(start)
        intervals_end.append(end)
    dots_coords = list(map(int, input().split()))
  
    retval = []
    intervals_start = sorted(intervals_start)
    intervals_end = sorted(intervals_end)
    for dot in dots_coords:
        n = binary_search(intervals_start, 0, len(intervals_start)-1, dot)
        m = binary_search(intervals_end, 0, len(intervals_end)-1, dot, True)
        retval.append(n-m)
    print(*retval)

if __name__ == "__main__":
    main()

