from __future__ import annotations

import sys
import pysam
import argparse

from cstag_cli.utils.io import read_sam
from cstag_cli.append.appender import append


def run_append(args):
    if args.file:
        sam: pysam.AlignmentFile = read_sam(args.file)
    else:
        sam: pysam.AlignmentFile = read_sam(sys.stdin)
    append(sam, args.long)


def main():
    parser = argparse.ArgumentParser(description="cstag command-line tool")
    subparsers = parser.add_subparsers(title="subcommands", description="valid subcommands", help="additional help")

    # cstag append
    append_parser = subparsers.add_parser("append", help="Append cs tag to SAM/BAM file")
    append_parser.add_argument("-f", "--file", type=str, help="Input path of SAM/BAM file")
    append_parser.add_argument("-l", "--long", help="Output long format of cs tag", action="store_true")
    append_parser.set_defaults(func=run_append)

    args = parser.parse_args()
    if "func" in args:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
