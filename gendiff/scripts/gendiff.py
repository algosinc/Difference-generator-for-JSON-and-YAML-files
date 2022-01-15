#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gendiff.cli import cli
from gendiff.generate_diff import generate_diff
from gendiff.constants import DEFAULT_FORMAT


def main():
    first_file, second_file, formatter_style = cli()
    diff = generate_diff(first_file, second_file, formatter_style=DEFAULT_FORMAT)
    print(diff)


if __name__ == '__main__':
    main()
