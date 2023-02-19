from sys import stdin

def read_from_stdin():
    print("Type coefficient matrix with columns divided by whitespace and rows by \"\\n\"")
    matrix = []

    try:
        while True:
            line = input()
            if line == '':
                break
            data = line.strip().split(" ")
            data = [float(i) for i in data]
            matrix.append(data)
    except EOFError:
        pass
    except Exception as e:
        print(f"Error: {e}")
        return None

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