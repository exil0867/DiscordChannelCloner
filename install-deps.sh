#!/usr/bin/env bash

DEBIAN_FRONTEND=noninteractive apt -y update

sudo apt install curl -y

curl -sSL https://install.python-poetry.org | python3 -

poetry install