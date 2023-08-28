from __future__ import annotations

from pathlib import Path
import pysam


# def validate_proper_extension(path: str | Path, ext: str = ".sam") -> None:
#     file_ext = Path(path).suffix
#     if file_ext != ext:
#         raise ValueError(f"Invalid file extension: {file_ext}")


# def validate_text_input_from_stdin(file_obj) -> None:
#     for line_count, line in enumerate(file_obj, start=1):
#         # Stop after reading the first 100 lines
#         if line_count > 100:
#             break
#         # Convert the line to bytes
#         data = line.encode("utf-8")
#         # Check if the data is binary
#         if any(b > 0x7F for b in data):
#             raise ValueError(f"Binary data detected.")


# def _is_valid_sam_header(sam_list: list[list[str]]) -> bool:
#     has_header = False
#     for line in sam_list:
#         if not line[0].startswith("@"):
#             if not has_header:
#                 return False
#             else:
#                 return True
#         has_header = True
#         # @SQ line should have at least 3 fields: @SQ, SN:<name>, LN:<length>
#         if line[0] == "@SQ":
#             if len(line) < 3 or not line[1].startswith("SN:") or not line[2].startswith("LN:"):
#                 return False
#         # @PG line should have at least 2 fields: @PG, ID:<name>
#         elif line[0] == "@PG":
#             if len(line) < 2 or not line[1].startswith("ID:"):
#                 return False
#         # @CO line should have at least 2 fields: @CO, <comment>
#         elif line[0] == "@CO":
#             if len(line) < 2:
#                 return False
#     return True


# def _is_valid_sam_alignment(sam_list: list[list[str]]) -> bool:
#     """validate the alignments using 100 alignments."""
#     num_alignment = 0
#     for alignment in sam_list:
#         if alignment[0].startswith("@"):
#             continue
#         if len(alignment) < 11:
#             return False
#         if num_alignment > 100:
#             return True
#         num_alignment += 1


# def validate_proper_sam_format(sam_list: list[list[str]]) -> None:
#     if not _is_valid_sam_header(sam_list) and not _is_valid_sam_alignment(sam_list):
#         raise ValueError(f"Invalid SAM format.")


def validate_having_md_tag(sam: pysam.AlignmentFile) -> None:
    for i, read in enumerate(sam):
        if not read.has_tag("MD"):
            raise ValueError(f"MD tag is not found in the input.")
        if i > 100:
            break


# def validate_containing_md_tag(sam_list: list[list[str]]) -> None:
#     num_alignment = 0
#     for alignment in sam_list:
#         if alignment[0].startswith("@"):
#             continue
#         if num_alignment > 100:
#             break
#         tag_info = "".join(alignment[11:])
#         if "MD:Z:" not in tag_info:
#             raise ValueError(f"MD tag is not found in the input.")
#         num_alignment += 1
