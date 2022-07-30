#!/usr/bin/env python
from gendiff.pars import args
from gendiff.gendiff import generate_diff


def main():
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
