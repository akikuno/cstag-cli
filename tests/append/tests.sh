#!/bin/bash

set -eu

test_tmp_dir=$(mktemp -d)
trap 'rm -rf "$test_tmp_dir"' EXIT

#######################################
# From standard input
#######################################

# Short format
cat tests/append/data/example.sam |
    cstag append >"$test_tmp_dir/example_cs_short.sam"

# Long format
cat tests/append/data/example.sam |
    cstag append -l >"$test_tmp_dir/example_cs_long.sam"

if ! diff "$test_tmp_dir/example_cs_short.sam" tests/append/data/example_cs_short.sam; then
    exit 1
fi

if ! diff "$test_tmp_dir/example_cs_long.sam" tests/append/data/example_cs_long.sam; then
    exit 1
fi

#######################################
# From file (SAM)
#######################################

# Short format
cstag append tests/append/data/example.sam >"$test_tmp_dir/example_cs_short.sam"

# Long format
cstag append tests/append/data/example.sam -l >"$test_tmp_dir/example_cs_long.sam"

if ! diff "$test_tmp_dir/example_cs_short.sam" tests/append/data/example_cs_short.sam; then
    exit 1
fi

if ! diff "$test_tmp_dir/example_cs_long.sam" tests/append/data/example_cs_long.sam; then
    exit 1
fi

#######################################
# From file (BAM)
#######################################

# Short format
cstag append tests/append/data/example.bam |
    grep -v "@HD" >"$test_tmp_dir/example_cs_short.sam"

# Long format
cstag append tests/append/data/example.bam -l |
    grep -v "@HD" >"$test_tmp_dir/example_cs_long.sam"

if ! diff "$test_tmp_dir/example_cs_short.sam" tests/append/data/example_cs_short.sam; then
    exit 1
fi

if ! diff "$test_tmp_dir/example_cs_long.sam" tests/append/data/example_cs_long.sam; then
    exit 1
fi

#######################################
# No arguments
#######################################

cstag >"$test_tmp_dir/help.txt"

if ! diff "$test_tmp_dir/help.txt" tests/append/data/help.txt; then
    exit 1
fi
