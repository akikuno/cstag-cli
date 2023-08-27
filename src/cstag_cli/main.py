from __future__ import annotations

import os
import argparse
from typing import Generator

from cstag_cli.append.appender import append


def is_sam(path: str) -> bool | None:
    _, ext = os.path.splitext(path)
    if ext == ".sam":
        return True
    elif ext == ".bam":
        return False
    else:
        raise ValueError(f"Invalid file extension: {ext}")


def read_sam(path: str) -> Generator[list[str]]:
    pass


def read_bam(path: str) -> Generator[list[str]]:
    pass


def is_binary_data(data) -> bool:
    # ASCIIの範囲外のバイトが含まれているかチェックする
    return any(b > 0x7F for b in data)


def read_stdin(file_obj):
    for line in file_obj:
        data = line.encode("utf-8")  # Convert the line to bytes
        if is_binary_data(data):
            raise ValueError(f"Binary data detected.")
        yield data


def append_action(args):
    append()
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

    append_parser = subparsers.add_parser("append", help="Append data")
    append_parser.add_argument("-f", "--file", type=str, help="Input path of SAM/BAM file")
    append_parser.set_defaults(func=append_action)

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
