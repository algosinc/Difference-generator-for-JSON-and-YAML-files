#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gendiff.scripts.formatters.stylish import stylish_formatter
from gendiff.scripts.formatters.plain import plain_formatter
from tests.fixtures.formatters.diff_fixture import data

STYLISH_RESULT = r'tests/fixtures/formatters/stylish_result.txt'
PLAIN_RESULT = r'tests/fixtures/formatters/plain_result.txt'


def test_stylish_format():
    with open(STYLISH_RESULT, 'r') as result_file:
        assert stylish_formatter(data) == result_file.read()


def test_plain_format():
    with open(PLAIN_RESULT, 'r') as result_file:
        assert plain_formatter(data) == result_file.read()
