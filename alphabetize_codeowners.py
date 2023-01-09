#!/usr/bin/env python
"""
Alphabetize the list of owners for each path in .github/CODEOWNERS

Ignores empty lines and comments, but normalizes whitespace on semantically significant
lines
"""

import argparse
import pathlib
import re
import sys

__version__ = "0.0.1"

WS_PAT = re.compile(r"\s+")


def main() -> None:
    # argparser stub for now
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "FILES", nargs="*", help="codeowners file (defaults to .github/CODEOWNERS)"
    )
    parser.add_argument("-v", "--verbose", help="enable verbose mode", action="count")
    args = parser.parse_args()

    filenames = list(args.FILES)
    if not filenames:
        filenames = [".github/CODEOWNERS"]

    exit_code = 0
    for fname in filenames:
        exit_code |= handle_file(fname, verbose=bool(args.verbose))
    sys.exit(exit_code)


def handle_file(fname: str, *, verbose: bool) -> int:
    co_path = pathlib.Path(fname)
    if not co_path.exists():
        print(f"'{fname}' does not exist", file=sys.stderr)
        sys.exit(2)

    content = co_path.read_text()
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        if line == "" or line.strip().startswith("#"):
            new_lines.append(line)
        else:
            new_lines.append(sort_line(line))

    new_content = "\n".join(new_lines)
    co_path.write_text(new_content)

    if new_content != content:
        if verbose:
            print("modified codeowners")
        return 1

    if verbose:
        print("ok")
    return 0


def sort_line(line: str) -> str:
    # also normalizes whitespace
    dedented = line.lstrip()
    elements = WS_PAT.split(dedented)
    path = elements[0]
    owners = sorted(elements[1:])
    return " ".join([path] + owners)


if __name__ == "__main__":
    main()
