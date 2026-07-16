def read_file_safely(name):
    try:
        print(open(name).read())
    except FileNotFoundError:
        print('File not found')

read_file_safely('test.txt')
