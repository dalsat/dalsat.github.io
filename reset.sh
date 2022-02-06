#!/usr/bin/env bash

rm -rf venv &&
python3 -m venv --upgrade-deps venv &&
./venv/bin/pip3 install --upgrade -r requirements.txt