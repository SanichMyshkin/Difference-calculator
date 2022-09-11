import argparse


def gendiff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    # parser = argparse.ArgumentParser(prog='gendiff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(args)
