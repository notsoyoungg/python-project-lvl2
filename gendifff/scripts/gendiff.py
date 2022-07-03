#!/usr/bin/env python
from gendifff.modules import make_diff
from gendifff.modules import pars


def main():
    print(make_diff.generate_diff(pars.readed, pars.readed2))


if __name__ == '__main__':
    main()
