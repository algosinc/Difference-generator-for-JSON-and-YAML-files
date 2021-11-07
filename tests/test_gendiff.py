# -*- coding:utf-8 -*-

from gendiff.scripts.gendiff import generate_diff

PATH_TO_JSON_1_FILE = 'tests/fixtures/json/file1.json'
PATH_TO_JSON_2_FILE = 'tests/fixtures/json/file2.json'
PATH_TO_JSON_RESULT_FILE = 'tests/fixtures/json/json_result.txt'


def test_generate_diff():
    with open(PATH_TO_JSON_RESULT_FILE, 'r') as result_file:
        result = result_file.read()
        assert generate_diff(
            PATH_TO_JSON_1_FILE, PATH_TO_JSON_2_FILE, 'format') == result
