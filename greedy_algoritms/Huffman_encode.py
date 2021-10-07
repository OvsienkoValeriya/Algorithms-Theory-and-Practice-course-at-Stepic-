#По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита, #постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, #встречающихся в строке, и размер получившейся закодированной строки. В следующих k строках #запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку.

class TreeNode:
    def __init__(self, value, weight, left_child, right_child):
        self.value = value
        self.weight = weight
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return f'({self.value}, w: {self.weight}, left:{self.left_child}, right:{self.right_child})'

def newNode( data, weight):
    return TreeNode(data, weight, None, None)

def split(word):
    lst = [char for char in word]
    counted = dict((x,lst.count(x)) for x in set(lst))
    sorted_dict = dict(sorted(counted.items(), key=lambda item: item[1], reverse = False))  
    return sorted_dict

def node_creation(word):
    dictionary = split(word)
    lst = []
    for char in dictionary:
        lst.append(newNode(char, dictionary[char]))
    while len(lst) > 1:
        left = lst.pop(0)
        right = lst.pop(0)
        lst.append(TreeNode(None, left.weight+right.weight, left, right))
        lst.sort(key=lambda x: x.weight)
    return lst[0]

dict_paths = {}
def recursive_tree(node, path):
    if node.left_child:
        recursive_tree(node.left_child, path+'0')
    if node.right_child:
        recursive_tree(node.right_child, path+'1')
    if node.value:
        dict_paths[node.value] = path

def code(word):
    lst = [char for char in word]
    coded = ""
    for char in lst:
        coded += dict_paths[char]
    return coded

def main():  
    word = str(input())
    lst = [char for char in word]
    counted = dict((x,lst.count(x)) for x in set(lst))
    if len(counted) == 1:
        recursive_tree(node_creation(word), '0')
    else:
        recursive_tree(node_creation(word), '')
    print(f'{len(counted)} {len(code(word))}')
    for path in dict_paths:
        print(f'{path}: {dict_paths[path]}')
    print(code(word))  


if __name__ == "__main__":
    main()

