from __future__ import annotations

import os
import sys
import argparse
from typing import Generator

from cstag_cli.utils.io import read_sam
from cstag_cli.append.appender import append


def run_append(args):
    if args.file:
        sam = read_sam(args.file)
    else:
        sam = read_sam(sys.stdin)
    append(sam, args.long)
    # if args.file:
    #     if is_sam(args.file):
    #         data = read_sam(args.file)
    #     else:
    #         data = read_bam(args.file)
    # else:
    #     data = read_stdin(sys.stdin)
    # print(args)


def main():
    parser = argparse.ArgumentParser(description="cstag command-line tool")
    subparsers = parser.add_subparsers(title="subcommands", description="valid subcommands", help="additional help")

    # cstag append
    append_parser = subparsers.add_parser("append", help="Append data")
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


# def main():
#     parser = argparse.ArgumentParser(description="Process some data.")
#     parser.add_argument("-f", "--file", type=str, help="Input path of SAM/BAM file")
#     args = parser.parse_args()

#     if args.file:
#         with open(args.file, "r") as f:
#             data = f.read()
#     else:
#         data = sys.stdin.read()

#     # 以下に、dataを処理するコードを書く
#     print(f"Received data: {data}")


# if __name__ == "__main__":
#     main()


# def execute():
#     print("TEST")
#     print(np.zeros(10))
#     sys.exit(0)
