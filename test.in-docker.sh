#!/bin/bash
#
# Expected parameter: <test_name> where test_name is a name of the test file from `tests/` folder.

pip install -r requirements.txt > /dev/null 2>&1
python "tests/$1"
