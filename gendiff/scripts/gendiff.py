#!/usr/bin/env python3
import argparse
from gendiff.engine import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')  # noqa E501
    parser.add_argument('-f', '--format',
                        default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output')
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file,formater=args.format))


if __name__ == "__main__":
    main()
