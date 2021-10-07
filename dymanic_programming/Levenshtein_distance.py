#Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2, содержащих #строчные буквы латинского алфавита.

def editDistBU(word1, word2):
    arrA = [a for a in word1]
    arrA.insert(0, '0')
    arrB = [b for b in word2]
    arrB.insert(0, '0')  
    n, m = len(word1), len(word2)
    matrix = [[0 for x in range(n+1)] for y in range(m+1)] 
    for i in range(0,m+1):
        matrix[i][0] = i    
    for j in range(0,n+1):
        matrix[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            c = diff(arrB[i], arrA[j])
            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+c)
      
    return matrix[m][n]
   

def diff(char1, char2):
    if char1 == char2:
        return 0
    else:
        return 1

def main():
    words = []
    for _ in range(2):
        words.append(str(input()))
    print(editDistBU(words[0], words[1]))

if __name__ == "__main__":
    main()
