#!/bin/bash

version_main=$(cstag -v)
version_pyproject=$(grep version pyproject.toml | cut -d " " -f 3 | sed -e 's/"//g')

if [ "$version_main" != "$version_pyproject" ]; then
    echo "Version mismatch: $version_main != $version_pyproject"
    exit 1
fi
