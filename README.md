[![Licence](https://img.shields.io/badge/License-MIT-9cf.svg)](https://choosealicense.com/licenses/mit/)
[![Test](https://img.shields.io/github/actions/workflow/status/akikuno/cstag-cli/pytest.yml?branch=main&label=Test&color=brightgreen)](https://github.com/akikuno/cstag/actions)
[![Python](https://img.shields.io/pypi/pyversions/cstag-cli.svg?label=Python&color=blue)](https://pypi.org/project/cstag-cli/)
[![PyPI](https://img.shields.io/pypi/v/cstag-cli.svg?label=PyPI&color=orange)](https://pypi.org/project/cstag-cli/)
[![Bioconda](https://img.shields.io/conda/v/bioconda/cstag-cli?label=Bioconda&color=orange)](https://anaconda.org/bioconda/cstag-cli)
[![DOI](https://zenodo.org/badge/683243028.svg)](https://zenodo.org/badge/latestdoi/683243028)


# cstag-cli

`cstag-cli` is a command-line tool of [`cstag`](https://github.com/akikuno/cstag) for manipulating [minimap2's CS tags](https://github.com/lh3/minimap2#the-cs-optional-tag).

## 🌟Features

- `cstag append`: Appends CS tags to a SAM/BAM file

## 🛠 Installation

Using [PyPI](https://pypi.org/project/cstag-cli/):

```bash
pip install cstag-cli
```

Using [Bioconda](https://anaconda.org/bioconda/cstag-cli):

```bash
conda install -c bioconda cstag-cli
```

## 💡Usage

### Appending CS Tags to a SAM/BAM File

```bash
cstag append <file> [-l/--long]
```

- **\<file\>**:  Path to the SAM/BAM file. If omitted, the program reads from standard input.  
> Note: The SAM/BAM file must contain an MD tag.
- **-l/--long**: Generates CS tags in long format

#### Examples

- Appending CS tags in short format:
```bash
cstag append tests/append/data/example.bam > example_cs_short.sam
```

- Appending CS tags in long format:
```bash
cstag append tests/append/data/example.bam --long > example_cs_long.sam
```
- Reading data from standard input:

```bash
cat tests/append/data/example.bam | cstag append > example_cs_short.sam
```

## 📣Feedback

For questions, bug reports, or other forms of feedback, we'd love to hear from you!  
Please use [GitHub Issues](https://github.com/akikuno/cstag-cli/issues) for all reporting purposes.  


Please note that this project is released with a [Contributor Code of Conduct](https://github.com/akikuno/cstag-cli/blob/main/CODE_OF_CONDUCT.md).  
By participating in this project you agree to abide by its terms.  
