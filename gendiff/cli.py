#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from gendiff.constants import STYLISH, PLAIN, JSON, DEFAULT_FORMAT


def cli():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f',
                        '--format',
                        choices=[STYLISH, PLAIN, JSON],
                        default=DEFAULT_FORMAT,
                        help='set format of output (default: JSON)')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
