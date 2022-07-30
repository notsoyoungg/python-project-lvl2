#!/usr/bin/env python
from gendiff import pars
from gendiff.gendiff import generate_diff


def main():
    print(generate_diff(pars.args.first_file, pars.args.second_file, pars.args.format))


if __name__ == '__main__':
    main()
