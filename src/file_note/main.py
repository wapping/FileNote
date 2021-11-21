# -*- coding: utf-8 -*-
import os
import sys
import logging
from argparse import ArgumentParser
from file_note.note import FileNote, filter_notes_by_keyword, formatted_print


logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.INFO)


def main():
    parser = ArgumentParser('file_note')
    parser.add_argument('--add', '-a', type=str, nargs='+', help='Add file note.')
    parser.add_argument('--add_relation', '-ar', type=str, nargs='+', help='Add file note.')
    parser.add_argument('--print_file', '-pf', action='store_true', help='Print the file table.')
    parser.add_argument('--print_relation', '-pr', type=str, help='Print the relationships of a given file.')
    parser.add_argument('--dir', '-d', type=str, help='Print the notes of files in the given dir.')
    parser.add_argument('--keyword', '-k', type=str, help='Print the notes of files with the given keyword.')
    parser.add_argument('--recursive', '-r', action='store_true', help='Print the notes of files in the given directory recursively.')
    parser.add_argument('--replace', '-rp', action='store_true', help='If replace the existing note.')
    args = parser.parse_args()

    fn = FileNote()
    if args.add:
        add = args.add
        assert len(add) == 2, 'The length of add must be 2.'
        fp, rmk = add
        if not os.path.exists(fp):
            raise FileNotFoundError(fp)
        else:
            fp = os.path.abspath(fp)
        fn.add_note(fp, rmk, args.replace)

    if args.add_relation:
        add_rel = args.add_relation
        if len(add_rel) == 3:
            fn.add_relation(*add_rel, '', replace=args.replace)
        elif len(add_rel) == 4:
            fn.add_relation(*add_rel, replace=args.replace)
        else:
            logging.error('The length of add_relation must be 3 or 4.')
            sys.exit()

    if args.print_file:
        if args.keyword:
            fn.file_table = filter_notes_by_keyword(fn.file_table, args.keyword)

        loc = os.path.abspath(args.dir) if args.dir else ''
        if not args.recursive:
            for k, v in fn.file_table.items():
                if loc:
                    d = os.path.split(k)[0]
                    if d == loc:
                        formatted_print(k, v)
                else:
                    formatted_print(k, v)
        else:
            fn.print_notes_recursively(args.dir)

    if args.print_relation:
        rel = args.print_relation
        fn.print_relationships(rel)


if __name__ == '__main__':
    main()
