#!/usr/bin/env bash

apt -y update

apt install curl -y

curl -sSL https://install.python-poetry.org | python3 -

poetry install
