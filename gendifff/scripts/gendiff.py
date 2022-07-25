#!/usr/bin/env python
from gendifff.modules import make_diff
from gendifff.modules import pars
from gendifff.modules import formatters


def main():
    print(formatters.generate_diff(make_diff.make_diff(pars.readed, pars.readed2)))


if __name__ == '__main__':
    main()
