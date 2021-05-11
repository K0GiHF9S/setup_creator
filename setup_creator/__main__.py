import argparse
import sys

from . import __version__

ENCODING = "utf-8"


def parse_args(args: list[str]):
    parser = argparse.ArgumentParser(prog="setup_creator")
    parser.add_argument(
        "-s",
        "--setting",
        nargs="+",
        type=argparse.FileType("r", encoding=ENCODING),
        default="setting.toml",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
