# -*- coding:utf-8 -*-
from gendiff.scripts.formatters.plain import plain_formatter

PATH_TO_RESULT_FILE = r'tests/fixtures/formatters/plain_result.txt'

data = \
    {
        'common': {
            'state': 'nested',
            'value': {
                'follow': {
                    'state': 'added',
                    'value': False
                },
                'setting1': {
                    'state': 'unchanged',
                    'value': 'Value 1'
                },
                'setting2': {
                    'state': 'removed',
                    'value': 200
                },
                'setting3': {
                    'state': 'changed',
                    'value': True,
                    'new_value': None
                },
                'setting4': {
                    'state': 'added',
                    'value': 'blah blah'
                },
                'setting5': {
                    'state': 'added',
                    'value': {
                        'key5': {
                            'state': 'unchanged',
                            'value': 'value5'
                        }
                    }
                },
                'setting6': {
                    'state': 'nested',
                    'value': {
                        'doge': {
                            'state': 'nested',
                            'value': {
                                'wow': {
                                    'state': 'changed',
                                    'value': '',
                                    'new_value': 'so much'
                                }
                            }
                        },
                        'key': {
                            'state': 'unchanged',
                            'value': 'value'
                        },
                        'ops': {
                            'state': 'added',
                            'value': 'vops'
                        }
                    }
                }
            }
        },
        'group1': {
            'state': 'nested',
            'value': {
                'baz': {
                    'state': 'changed',
                    'value': 'bas',
                    'new_value': 'bars'
                },
                'foo': {
                    'state': 'unchanged',
                    'value': 'bar'
                },
                'nest': {
                    'state': 'changed',
                    'value': {
                        'key': {
                            'state': 'unchanged',
                            'value': 'value'
                        }
                    },
                    'new_value': 'str'
                }
            }
        },
        'group2': {
            'state': 'removed',
            'value': {
                'abc': {
                    'state': 'unchanged',
                    'value': 12345
                },
                'deep': {
                    'state': 'unchanged',
                    'value': {
                        'id': {
                            'state': 'unchanged',
                            'value': 45
                        }
                    }
                }
            }
        },
        'group3': {
            'state': 'added',
            'value': {
                'deep': {
                    'state': 'unchanged',
                    'value': {
                        'id': {
                            'state': 'unchanged',
                            'value': {
                                'number': {
                                    'state': 'unchanged',
                                    'value': 45
                                }
                            }
                        }
                    }
                },
                'fee': {
                    'state': 'unchanged',
                    'value': 100500
                }
            }
        }
    }

plain_formatter(data)

# def test_stylish_format():
#     with open(PATH_TO_RESULT_FILE, 'r') as result_file:
#         assert plain_formatter(data) == result_file.read()
