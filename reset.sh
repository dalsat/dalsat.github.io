#!/usr/bin/env bash

rm -rf venv
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip && pip install --upgrade -r requirements.txt