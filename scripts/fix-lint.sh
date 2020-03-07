#!/bin/bash

pipenv run flake8 | awk -F ":" '{print $1}' | xargs pipenv run autopep8 --in-place ${@}