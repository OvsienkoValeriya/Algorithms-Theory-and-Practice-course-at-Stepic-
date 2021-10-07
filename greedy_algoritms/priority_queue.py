#Первая строка входа содержит число операций 1≤n≤10^5. Каждая из последующих n строк задают #операцию одного из следующих двух типов:
#
#    Insert x, где 0≤x≤10^9 — целое число;
#    ExtractMax.
#
#Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное #число и выводит его.

tree = [0]  
def insert(value):
    tree.append(int(value))
    tree_height = len(tree) - 1
  
    while (tree_height // 2) > 0:
        if tree[tree_height] > tree[tree_height // 2]:
            temp = tree[tree_height // 2]
            tree[tree_height // 2] = tree[tree_height]
            tree[tree_height] = temp
        tree_height = tree_height // 2     
    
def get_max_child(i, tree_height):
    child_1 = 2*i
    child_2 = 2*i+1
    if child_2 > tree_height:
        return child_1
    else:
        if tree[child_1]<tree[child_2]:
            return child_2
        else:
            return child_1


def extract_max():
    retval = tree[1]
    end = tree.pop(-1)
    tree_height = len(tree)-1
    if tree_height != 0:
        tree[1] = end
    else:
        return retval
    i=1
    while i*2 <= tree_height:
        max_child = get_max_child(i, tree_height)
        if tree[i] < tree[max_child]:
            temp = tree[i]
            tree[i] = tree[max_child]
            tree[max_child] = temp
        i = max_child
    return retval

def readCommands():
    commands_count = int(input())
    for c in range(commands_count):
        command = input()
        if command == "ExtractMax":      
            print(extract_max())
        else:
            com, value = command.split()
            insert(value)
    
def main():  
    readCommands()

if __name__ == "__main__":
    main()

