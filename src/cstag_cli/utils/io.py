from __future__ import annotations
from pathlib import Path
from typing import Generator
import bamnostic as bs
import pysam
from pysam import AlignmentHeader, AlignmentFile
import sys


def read_sam_lines_as_generator(path_sam: str | Path) -> Generator[str]:
    with open(path_sam, "r") as f:
        for line in f:
            yield line.strip()


def read_sam_lines_as_list(path_sam: str | Path) -> list[str]:
    with open(path_sam, "r") as f:
        return [line.strip() for line in f.readlines()]


def read_bam_lines_as_generator(path_bam: str | Path) -> Generator[str]:
    bam = bs.AlignmentFile(str(path_bam), "rb")
    with open(path_bam, "r") as f:
        for line in f:
            yield line.strip()


def read_bam_lines_as_list(path_bam: str | Path) -> list[str]:
    with open(path_bam, "r") as f:
        return [line.strip() for line in f.readlines()]


def output_sam_to_stdout(header: AlignmentHeader, bam: AlignmentFile) -> None:
    with pysam.AlignmentFile(sys.stdout, "wh", header=header) as sam_file:
        for read in bam:
            sam_file.write(read)
