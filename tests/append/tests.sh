#!/bin/bash

#######################################
# From standart input
#######################################

# Short format
cat tests/append/data/example.sam |
    cstag append >/tmp/example_cs_short.sam

# Long format
cat tests/append/data/example.sam |
    cstag append -l >tests/append/data/example_cs_long.sam

if ! diff /tmp/example_cs_short.sam tests/append/data/example_cs_short.sam; then
    exit 1
fi

if ! diff /tmp/example_cs_long.sam tests/append/data/example_cs_long.sam; then
    exit 1
fi

#######################################
# From file (SAM)
#######################################

# Short format
cstag append -f tests/append/data/example.sam >/tmp/example_cs_short.sam

# Long format
cstag append -f tests/append/data/example.sam -l >tests/append/data/example_cs_long.sam

if ! diff /tmp/example_cs_short.sam tests/append/data/example_cs_short.sam; then
    exit 1
fi

if ! diff /tmp/example_cs_long.sam tests/append/data/example_cs_long.sam; then
    exit 1
fi

#######################################
# From file (BAM)
#######################################

# Short format
cstag append -f tests/append/data/example.bam |
    grep -v "@HD" >/tmp/example_cs_short.sam

# Long format
cstag append -f tests/append/data/example.bam -l |
    grep -v "@HD" >tests/append/data/example_cs_long.sam

if ! diff /tmp/example_cs_short.sam tests/append/data/example_cs_short.sam; then
    exit 1
fi

if ! diff /tmp/example_cs_long.sam tests/append/data/example_cs_long.sam; then
    exit 1
fi
