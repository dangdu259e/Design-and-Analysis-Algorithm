def getMatrix_txt(filename):
    file = open(filename, 'r')
    matrix = [[int(number) for number in line.split()] for line in file]  # đọc file txt theo dòng và từng cột của dòng
    return matrix


def find_way_matrix(matrix):
    return 0


matrix = getMatrix_txt("matrix.txt")
print(matrix)
