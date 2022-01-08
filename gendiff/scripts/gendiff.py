#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gendiff.cli import cli
from gendiff.generate_diff import generate_diff


def main():
    first_file, second_file, parse_format = cli()
    diff = generate_diff(first_file, second_file, parse_format)
    print(diff)


if __name__ == '__main__':
    main()
