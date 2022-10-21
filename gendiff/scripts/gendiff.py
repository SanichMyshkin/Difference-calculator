#!/usr/bin/env python3
from gendiff.engine import generate_diff
from gendiff.cli import parse_args


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file,
                        formater=args.format))


if __name__ == "__main__":
    main()
