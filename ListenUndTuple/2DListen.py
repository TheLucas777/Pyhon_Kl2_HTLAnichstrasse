liste = [[1,2,3],[4,27,6,3],[7,8,9]]

def print_table(table):
    for row in table:
        for element in row:
            print(element, end=" ")
        print()

print_table(liste)