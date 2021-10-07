#Восстановите строку по её коду и беспрефиксному коду символов. 
#
#В первой строке входного файла заданы два целых числа k и l через пробел — количество различных #букв, встречающихся в строке, и размер получившейся закодированной строки, соответственно. В #следующих k строках записаны коды букв в формате "letter: code". Ни один код не является #префиксом другого. Буквы могут быть перечислены в любом порядке. В качестве букв могут #встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке #хотя бы один раз. Наконец, в последней строке записана закодированная строка. Исходная строка и #коды всех букв непусты. Заданный код таков, что закодированная строка имеет минимальный возможный #размер.
#
#В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв #латинского алфавита. Гарантируется, что длина правильного ответа не превосходит 10^4 символов.

def readCodes():
    letters_count, str_len = map(int, input().split())
    code_dict = {}
    for letter in range(letters_count):
        k, v = map(str, input().split(': '))
        code_dict.update({v: k})
    coded_string = input()
    decoded = ""
    coded = [char for char in coded_string]
    unknown = ''
    for i in range(str_len):
        unknown = unknown + coded[i]
        if unknown in code_dict:
            decoded += code_dict[unknown]
            unknown = ''
        else:
            continue
    return decoded
  
def main():  
    print(readCodes())

if __name__ == "__main__":
    main()
