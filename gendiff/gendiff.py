import argparse


def gendiff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', "--format", help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(args)
    # parser.print_help() # тоже самое что и gendiff -h , но нам не нужно собирать проект

# poetry run gendiff -h
# python3 -m pip install . gendiff
# gendiff -h
