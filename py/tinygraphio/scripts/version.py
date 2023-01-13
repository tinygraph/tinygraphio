from tinygraphio.reader import TinygraphioReader


def main(args):
    with args.tinygraph.open("rb") as f:
        reader = TinygraphioReader(f)
        header = reader._read_file_header()

        print(header.version)
