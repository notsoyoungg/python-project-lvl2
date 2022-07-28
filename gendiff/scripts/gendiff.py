#!/usr/bin/env python
from gendiff.modules.make_diff import make_diff
from gendiff.modules import pars
from gendiff.modules.gendiff import generate_diff


def main():
    print(generate_diff(make_diff(pars.readed, pars.readed2), pars.args.format))


if __name__ == '__main__':
    main()
