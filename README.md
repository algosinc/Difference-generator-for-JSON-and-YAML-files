# Difference generator (Gendiff)
[![linter-and-test-check](https://github.com/Corrosion667/python-project-lvl2/actions/workflows/linter-and-test-check.yml/badge.svg)](https://github.com/Corrosion667/python-project-lvl2/actions/workflows/linter-and-test-check.yml)
[![Actions Status](https://github.com/algosinc/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/algosinc/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/f3994705cf70aae343a6/maintainability)](https://codeclimate.com/github/algosinc/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f3994705cf70aae343a6/test_coverage)](https://codeclimate.com/github/algosinc/python-project-lvl2/test_coverage)
---

**The difference generator** *(further - gendiff)* is a program that determines the difference between two data structures. The difference is presented in one of three formats to choose from. Gendiff is currently working with **JSON** and **YML/YAML** files.


## Quickstart

**Gendiff** is stored only at GitHub at the moment so the quickest and easiest way to install it is to use pip with the URL of the repository.
```bash
pip install git+https://github.com/algosinc/python-project-lvl2.git
```

## Running

Basic **Gendiff** syntax looks like this:
```bash
gendiff --format path/to/file1 path/to/file2
```
The **format** is an optional argument. The default value is *'stylish'*. But all three formatters are described below.

You can also recall about main features and syntax of a program using the *help command*:
```bash
gendiff -h
```

## Formatters

As was said above, there are three formatters that gendiff is currently supporting:

|   **Formatter**   |                                    **Description**                                    |
|-------------------|---------------------------------------------------------------------------------------|
|     **stylish**     | default one; JSON-like format with '-' for deleted elements and '+' for added         |       
|      **plain**      | thesis-like format with statements about adding, updating and removal of elements      |      
|      **json**       | classic JSON; list of lists with following structure: [key, status, value(s)]         |

The work of different formatters will be demonstrated below by using asciinema service.

## Asciinema demonstrations:

Installation, launch help menu and usage examples:

[![asciicast](https://asciinema.org/a/wzugT96j90lbCmbgWcnguY6Yc.svg)](https://asciinema.org/a/wzugT96j90lbCmbgWcnguY6Yc)

