#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args, help):
    '''
    Simple line numbering program to demonstrate CLI interface
    '''

    if not (select.select([sys.stdin,],[],[],0.0)[0] or args.files):
        help()
        return

    try:
        for i, line in enumerate(fileinput.input(args.files)):
            print i + 1, line.strip()
    except IOError:
        sys.stderr.write("%s: No such file %s\n" % (os.path.basename(__file__), fileinput.filename()))

if __name__ == "__main__":
    import os, sys, select, argparse, fileinput
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', help='input files')
    main(parser.parse_args(), parser.print_help)
