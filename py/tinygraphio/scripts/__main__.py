import argparse
from pathlib import Path

import tinygraphio.scripts.version


def main():
    parser = argparse.ArgumentParser(prog="tinygraphio")
    Formatter = argparse.ArgumentDefaultsHelpFormatter

    subcmd = parser.add_subparsers(dest="command")
    subcmd.required = True

    version = subcmd.add_parser("version", formatter_class=Formatter)
    version.add_argument("tinygraph", type=Path, help="path to tinygraph")
    version.set_defaults(main=tinygraphio.scripts.version.main)

    args = parser.parse_args()
    args.main(args)


if __name__ == "__main__":
    main()
