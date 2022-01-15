
from gendiff.generate_diff import generate_diff
from gendiff.constants import DEFAULT_FORMAT

# first_file = r'../tests/fixtures/json/file1.json'
# second_file = r'../tests/fixtures/json/file2.json'

first_file = r'../tests/fixtures/yaml/file1.yml'
second_file = r'../tests/fixtures/yaml/file2.yml'


print(generate_diff(first_file, second_file, formatter_style=DEFAULT_FORMAT))

# print(generate_diff(first_file, second_file, 'stylish'))
# print(generate_diff(first_file, second_file))
