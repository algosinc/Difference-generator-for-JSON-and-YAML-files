#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gendiff.cli import cli
from gendiff.generate_diff import generate_diff


def main():
    """ Get data from CLI, run diff generation and print result """
    first_file, second_file, formatter_style = cli()
    diff = generate_diff(first_file, second_file, formatter_style)
    print(diff)


if __name__ == '__main__':
    main()
