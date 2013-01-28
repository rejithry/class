import os

def print_file_names(dir):
    for file_name in os.listdir(dir):
        print file_name
    print [2**i for i in range(10)]

if __name__ == '__main__':
    print_file_names('.')
