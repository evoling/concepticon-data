"""
Add an ID column based on the filename + sequential integer.
"""
import argparse
from os.path import splitext
from sys import stdout

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("infile", type=open, help="""Concepticon tab separated
            values file""")
    parser.add_argument("outfile", type=argparse.FileType("w"), 
            default=stdout, nargs="?", help="""Destination file""")
    args = parser.parse_args()
    header = next(args.infile).strip().split("\t")
    assert header[0] != "ID" and "ID" not in header
    base = splitext(args.infile.name)[0]
    print("ID", *header, sep="\t", file=args.outfile)
    for i, line in enumerate(args.infile):
        row = line.strip("\n").split("\t")
        ID = "{}-{}".format(base, i+1)
        print(ID, *row, sep="\t", file=args.outfile)
    return

if __name__ == "__main__":
    main()
