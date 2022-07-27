#!/usr/bin/env python
from gendifff.modules.make_diff import make_diff
from gendifff.modules import pars
from gendifff.modules.generate_diff import generate_diff


def main():
    print(generate_diff(make_diff(pars.readed, pars.readed2), pars.args.format))


if __name__ == '__main__':
    main()
