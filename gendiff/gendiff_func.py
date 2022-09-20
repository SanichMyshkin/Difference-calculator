import argparse
from engine import run_generate_diff


def gendiff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.') # noqa E501
    parser.add_argument("-f", '--format', metavar='FORMAT', help="set format of output")                     # noqa E501
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    args = parser.parse_args()
    run_generate_diff(args.first_file, args.second_file)
