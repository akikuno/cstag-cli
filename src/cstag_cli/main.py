from __future__ import annotations
import sys
import select
import argparse

from cstag_cli.utils.io import read_sam
from cstag_cli.append.appender import append


def validate_stdin(data: sys.stdin, subparser) -> None:
    """Validate if data is available on standard input."""
    rlist, _, _ = select.select([data], [], [], 0)
    if not rlist:
        subparser.print_help()
        sys.exit(0)


def run_append(args, subparser) -> None:
    """Execute the 'append' command."""
    if args.file == "-":
        validate_stdin(sys.stdin, subparser)
        sam = read_sam(sys.stdin)
    else:
        sam = read_sam(args.file)

    append(sam, args.long)


def main() -> None:
    """Main function for the command-line tool."""
    parser = argparse.ArgumentParser(description="cstag command-line tool")
    parser.add_argument("-v", "--version", action="version", version="1.0.0")

    subparsers = parser.add_subparsers(dest="command", description="valid subcommands", help="additional help")
    subparsers_dict = {}

    # Subparser for 'cstag append'
    append_parser = subparsers.add_parser("append", help="Append CS tag to SAM/BAM file")
    append_parser.add_argument("file", nargs="?", default="-", type=str, help="Input path of SAM/BAM file")
    append_parser.add_argument("-l", "--long", help="Output long format of CS tag", action="store_true")
    append_parser.set_defaults(func=run_append)
    subparsers_dict["append"] = append_parser

    args = parser.parse_args()

    if "func" in args:
        args.func(args, subparsers_dict.get(args.command))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
