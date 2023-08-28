from __future__ import annotations

import sys
import pysam


def is_binary_data(data: bytes) -> bool:
    """Check if a byte sequence contains binary data."""
    text_characters = b"".join(bytes([i]) for i in range(32, 127)) + b"\n\r\t\f\b"
    return bool(data.translate(None, text_characters))


def determine_format(input_stream):
    first_bytes = input_stream.read(100)

    # Seek back to the original position after reading bytes from the buffer
    input_stream.seek(0)

    if is_binary_data(first_bytes):
        return "BAM", "rb"
    elif first_bytes.startswith(b"@"):
        return "SAM", "r"
    else:
        return "Unknown", None


def read_sam(path_file: str) -> pysam.AlignmentFile:
    if path_file:
        with open(path_file, "rb") as file_stream:
            format, mode = determine_format(file_stream)
        input_stream = path_file
    else:
        format, mode = determine_format(sys.stdin.buffer)
        input_stream = sys.stdin.buffer if mode == "rb" else sys.stdin

    if format == "Unknown":
        raise ValueError("The input stream is neither in SAM nor in BAM format.")

    return pysam.AlignmentFile(input_stream, mode)


def write_sam(sam: pysam.AlignmentFile) -> None:
    # output header
    for record, fields in sam.header.to_dict().items():
        for field in fields:
            line = [f"@{record}"]
            for tag, value in field.items():
                line.append(f"{tag}:{value}")
            sys.stdout.write("\t".join(line) + "\n")
    # output body
    for read in sam:
        sys.stdout.write(read.to_string() + "\n")
