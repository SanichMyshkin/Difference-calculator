import argparse
from gendiff.engine import run_generate_diff



def gendiff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("-f", '--format', metavar='FORMAT', help="set format of output")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    args = parser.parse_args()
    run_generate_diff(args.first_file, args.second_file)
    # parser.print_help() # тоже самое что и gendiff -h , но нам не нужно собирать проект

# poetry run gendiff -h
# python3 -m pip install . gendiff
# gendiff -h
