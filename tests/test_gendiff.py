# -*- coding:utf-8 -*-

from gendiff.scripts.gendiff import generate_diff

PATH_TO_JSON_1_FILE = 'tests/fixtures/json/file1.json'
PATH_TO_JSON_2_FILE = 'tests/fixtures/json/file2.json'
PATH_TO_JSON_RESULT_FILE = 'tests/fixtures/json/json_result_stylish.txt'

PATH_TO_YAML_1_FILE = 'tests/fixtures/yaml/file1.yml'
PATH_TO_YAML_2_FILE = 'tests/fixtures/yaml/file2.yml'
PATH_TO_YAML_RESULT_FILE = 'tests/fixtures/yaml/yml_result_stylish.txt'


def test_generate_diff_json():
    with open(PATH_TO_JSON_RESULT_FILE, 'r') as result_file:
        result = result_file.read()
        print(f'r: \n{result}')
        func_result = generate_diff(PATH_TO_JSON_1_FILE, PATH_TO_JSON_2_FILE, 'stylish')
        print(f'fr: \n{func_result}')
        assert func_result == result


def test_generate_diff_yaml():
    with open(PATH_TO_YAML_RESULT_FILE, 'r') as result_file:
        result = result_file.read()
        diff = generate_diff(PATH_TO_YAML_1_FILE, PATH_TO_YAML_2_FILE, 'stylish')
        with open('tests/fixtures/yaml/yml_result.txt', 'w') as diff_result:
            diff_result.write(diff)
        assert diff == result
