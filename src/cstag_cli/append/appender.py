from __future__ import annotations
import pysam
import cstag


def append(sam: pysam.AlignmentFile, long: bool = False) -> None:
    """Append CS tags to reads in a SAM/BAM file.

    Args:
        sam (pysam.AlignmentFile): SAM/BAM file object.
        long (bool, optional): Whether to output CS tags in long format. Defaults to False.
    """

    # Output the header
    print(sam.header, end="")

    # Process each read in the SAM/BAM file
    for read in sam:
        if read.is_unmapped or read.query_sequence is None:
            print(read.to_string())
            continue

        # Check for the presence of the MD tag
        if not read.has_tag("MD"):
            raise ValueError(f"MD tag is not found in the input. \nThis error occurred at {read.query_name}.")

        # Append CS tag and output alignments
        try:
            cs = cstag.call(cigar=read.cigarstring, md=read.get_tag("MD"), seq=read.seq, long=long)
        except Exception as e:
            raise type(e)(f"{e}. \nThis error occurred at {read.query_name}.")

        # Set the CS tag for the read
        read.set_tag("cs", cs.replace("cs:Z:", ""), replace=True)

        # Output the modified read
        print(read.to_string())
