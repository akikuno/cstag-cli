# cstag-cli

A command-line tool of [`cstag`](https://github.com/akikuno/cstag) for manipulating [minimap2's cs tag](https://github.com/lh3/minimap2#the-cs-optional-tag).

## Features

- `cstag append`: Appends cs tags to a SAM/BAM file

## Usage

### `cstag append`

```bash
cstag append [-f/--file] [-l/--long]
```

- -f/--file: Specifies the path to a SAM/BAM file. If no file is provided, it reads from standard input. An MD tag is required in the SAM/BAM file.
- -l/--long: Outputs cs tags in the long format

#### Examples

- To append cs tags in theshort format:
```bash
cstag append -f tests/append/data/example.bam > example_cs_short.sam
```

- To append cs tags in the long format:
```bash
cstag append -f tests/append/data/example.bam -l > example_cs_long.sam
```
- Reading data from standard input:
```bash
cat tests/append/data/example.bam | cstag append > example_cs_short.sam
```

## Feedback

For questions, bug reports, or any other inquiries, feel free to reach out!
Please use [GitHub Issues](https://github.com/akikuno/cstag-cli/issues) for reporting.
