#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pip install pytest
py.test -x -vv -s $DIR/../tests/
