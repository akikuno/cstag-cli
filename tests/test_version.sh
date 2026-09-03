#!/bin/bash

set -eu

version_main=$(cstag -v)
version_pyproject=$(python -c 'import tomllib; file = open("pyproject.toml", "rb"); print(tomllib.load(file)["project"]["version"]); file.close()')

if [ "$version_main" != "$version_pyproject" ]; then
    echo "Version mismatch: $version_main != $version_pyproject"
    exit 1
fi
