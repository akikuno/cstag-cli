# Troubleshooting Guide

## Installation

### Prerequisites

- Python 3.11 or later
- A Unix-like environment such as Linux, macOS, or WSL
- An isolated Conda environment or Python virtual environment is recommended

### Conda or Mamba

Bioconda provides packages for supported Linux and macOS architectures. Create
an isolated environment so that `cstag-cli` and its `pysam` dependency do not
conflict with system packages:

```bash
conda create -n cstag-env -c conda-forge -c bioconda python=3.11 cstag-cli
conda activate cstag-env
```

The same command can be used with `mamba` in place of `conda`.

### pip

Current `pysam` releases provide wheels for common supported platforms. Upgrade
pip inside a virtual environment before installing so that an available wheel
can be selected:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install cstag-cli
```

If pip cannot find a compatible wheel, it may attempt a source build that needs
platform-specific compiler and htslib prerequisites. In that case, use the
Conda/Bioconda installation above or consult the current
[`pysam` installation documentation](https://pysam.readthedocs.io/en/latest/installation.html).

Windows users should use WSL because Bioconda does not provide native Windows
packages.

## Reporting other problems

Please use [GitHub Issues](https://github.com/akikuno/cstag-cli/issues) and
include the cstag-cli, Python, operating-system, and input-format versions.
