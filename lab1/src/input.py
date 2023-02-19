from sys import stdin

def read_from_stdin():
    
    print("Type coefficient matrix with colums devided by whitspace and rows by \"\\n\"")
    matrix = []

    for line in stdin:
        if line == '' or line == 'end\n':
            break
        data = line.strip().split(" ")
        data = [float(i) for i in data]

        matrix.append(data)


    return matrix

def read_from_file(filename):
    f = open(filename, "r")
    matrix = []
    data = f.readline().strip().split(" ")
    data = [float(i) for i in data]

    for line in range (len(data) - 2):
        matrix.append(data)
        data = f.readline().strip().split(" ")
        data = [float(i) for i in data]
    matrix.append(data)
    return matrix