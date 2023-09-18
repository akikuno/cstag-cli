from __future__ import annotations

import sys
import pysam
import select
import argparse

from cstag_cli.utils.io import read_sam
from cstag_cli.append.appender import append


def read_from_stdin(data: sys.stdin, subparser) -> sys.stdin:
    # Check if there is data to read from stdin
    rlist, _, _ = select.select([data], [], [], 0)

    if rlist:
        return data
    else:
        subparser.print_help()
        sys.exit(0)


def run_append(args, subparser):
    if args.file:
        sam: pysam.AlignmentFile = read_sam(args.file)
    else:
        sam: pysam.AlignmentFile = read_sam(read_from_stdin(sys.stdin, subparser))
    append(sam, args.long)


def main():
    parser = argparse.ArgumentParser(description="cstag command-line tool")
    subparsers = parser.add_subparsers(dest="command", description="valid subcommands", help="additional help")
    subparsers_dict = {}

    # cstag append
    append_parser = subparsers.add_parser("append", help="Append cs tag to SAM/BAM file")
    append_parser.add_argument("-f", "--file", type=str, help="Input path of SAM/BAM file")
    append_parser.add_argument("-l", "--long", help="Output long format of cs tag", action="store_true")
    append_parser.set_defaults(func=run_append)
    subparsers_dict["append"] = append_parser

    args = parser.parse_args()
    if "func" in args:
        args.func(args, subparsers_dict.get(args.command))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
