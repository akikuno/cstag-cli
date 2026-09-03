from __future__ import annotations

import argparse
import select
import sys
from collections.abc import Callable
from importlib.metadata import version
from typing import TextIO, cast

from .append.appender import append
from .utils.io import read_sam

CSTAG_CLI_VERSION = version("cstag-cli")


def validate_stdin(data: TextIO, subparser: argparse.ArgumentParser) -> None:
    """Validate if data is available on standard input."""
    rlist, _, _ = select.select([data], [], [], 0)
    if not rlist:
        subparser.print_help()
        sys.exit(0)


def run_append(
    args: argparse.Namespace,
    subparser: argparse.ArgumentParser,
) -> None:
    """Execute the 'append' command."""
    if args.file == "-":
        validate_stdin(sys.stdin, subparser)
        input_data: str | TextIO = sys.stdin
    else:
        input_data = cast(str, args.file)

    with read_sam(input_data) as sam:
        append(sam, cast(bool, args.long))


def main() -> None:
    """Main function for the command-line tool."""
    parser = argparse.ArgumentParser(description="cstag command-line tool")
    parser.add_argument("-v", "--version", action="version", version=CSTAG_CLI_VERSION)

    subparsers = parser.add_subparsers(
        dest="command", description="valid subcommands", help="additional help"
    )
    subparsers_dict: dict[str, argparse.ArgumentParser] = {}

    # Subparser for 'cstag append'
    append_parser = subparsers.add_parser(
        "append", help="Append a cs tag to SAM/BAM file"
    )
    append_parser.add_argument(
        "file", nargs="?", default="-", type=str, help="Input path of SAM/BAM file"
    )
    append_parser.add_argument(
        "-l", "--long", help="Output long format of a cs tag", action="store_true"
    )
    append_parser.set_defaults(func=run_append)
    subparsers_dict["append"] = append_parser

    args = parser.parse_args()

    if hasattr(args, "func"):
        command = cast(
            Callable[[argparse.Namespace, argparse.ArgumentParser], None],
            args.func,
        )
        command(args, cast(argparse.ArgumentParser, subparsers_dict.get(args.command)))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
