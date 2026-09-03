from __future__ import annotations

import sys
from typing import BinaryIO, TextIO

import pysam


def _is_binary_data(data: bytes) -> bool:
    """Check if a byte sequence contains binary data."""
    text_characters = b"".join(bytes([i]) for i in range(32, 127)) + b"\n\r\t\f\b"
    return bool(data.translate(None, text_characters))


def _determine_format(input_stream: BinaryIO) -> str:
    first_bytes = input_stream.read(100)

    # Check if the input stream is empty
    if not first_bytes:
        raise ValueError("The input is empty.")

    # Seek back to the original position after reading bytes from the buffer
    input_stream.seek(0)

    return "rb" if _is_binary_data(first_bytes) else "r"


def read_sam(data: str | TextIO) -> pysam.AlignmentFile:
    input_stream: str | TextIO
    if isinstance(data, str):
        with open(data, "rb") as file_stream:
            mode = _determine_format(file_stream)
        input_stream = data
    else:
        mode = "r"
        input_stream = sys.stdin
    return pysam.AlignmentFile(input_stream, mode)
