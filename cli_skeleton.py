#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args, help):
    '''
    Simple line numbering program to demonstrate CLI interface
    '''

    if not (select.select([sys.stdin,],[],[],0.0)[0] or args.files):
        help()
        return

    if args.output and args.output != '-':
        sys.stdout = open(args.output, 'w')

    try:
        for i, line in enumerate(fileinput.input(args.files, inplace=args.inplace)):
            print i + 1, line.strip()
    except IOError:
        sys.stderr.write("%s: No such file %s\n" % (os.path.basename(__file__), fileinput.filename()))

if __name__ == "__main__":
    import os, sys, select, argparse, fileinput
    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=30),
                                     description="A simple line numbering program to demonstrate a good CLI with python.")
    parser.add_argument('files', nargs='*', help='input files')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--inplace', action='store_true', help='modify files inplace')
    group.add_argument('-o', '--output', help='output file. The default is stdout')
    main(parser.parse_args(), parser.print_help)
