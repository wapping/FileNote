# -*- coding: utf-8 -*-
"""
Description :
Authors     : lihp
CreateDate  : 2021/11/20
"""
import os
import sys
import pickle
from enum import Enum
import logging
from .config import sep, table_dir, file_table_path, relation_table_path


logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.INFO)


class FileTreeNode:
    def __init__(self, data, sons):
        self.data = data
        self.sons = sons


class Relationship(Enum):
    Equal = 0
    Effect = 1


class FileNote:
    def __init__(self):
        self.table_dir = table_dir
        self.file_table_path = file_table_path
        self.relation_table_path = relation_table_path
        self.init_tables(self.table_dir)
        self.file_table = {}
        self.relation_table = {}
        self.read_tables()

    @staticmethod
    def init_tables(dire):
        """Init the data tables.
        """
        if not os.path.isdir(dire):
            os.makedirs(dire)

    def read_tables(self):
        """Read the existing data from tables."""
        if os.path.isfile(self.file_table_path):
            self.file_table = pickle.load(open(self.file_table_path, 'rb'))
        if os.path.isfile(self.relation_table_path):
            self.relation_table = pickle.load(open(self.relation_table_path, 'rb'))

    def add_note(self, fp, note, replace):
        if fp in self.file_table:
            if replace:
                self.file_table[fp] = note
                with open(self.file_table_path, 'wb') as f:
                    pickle.dump(self.file_table, f)
            else:
                print(f"The file has been noted. If you want to replace it, use '-rp' in your command.")
        else:
            self.file_table[fp] = note
            with open(self.file_table_path, 'wb') as f:
                pickle.dump(self.file_table, f)

    def add_relation(self, fp1, fp2, relation, note, replace):
        if not os.path.exists(fp1):
            logging.error(f"{fp1} not exists.")
            return
        elif not os.path.exists(fp2):
            logging.error(f"{fp2} not exists.")
            return

        fp1 = os.path.abspath(fp1)
        fp2 = os.path.abspath(fp2)
        key1 = fp1 + sep + fp2
        key2 = fp2 + sep + fp1
        if (key1 in self.relation_table or key2 in self.relation_table) and not replace:
            logging.error(f"The relationship already exists. If you want to replace it, use '-rp' in your command.")
            return
        try:
            relation = int(relation)
        except ValueError:
            logging.error(f"Unexpected relationship: {relation}")
            return

        if relation not in Relationship.__dict__['_value2member_map_']:
            logging.error(f"Unexpected relationship: {relation}")
            return

        self.relation_table[key1] = (relation, note)
        with open(self.relation_table_path, 'wb') as f:
            pickle.dump(self.relation_table, f)

    def print_notes_recursively(self, dire):
        """Print notes of files in the given directory recursively.
        """
        # filter out the notes the directory
        dire = dire if dire else '/'
        dire = os.path.abspath(dire)
        notes = [(k.lstrip(dire).strip(os.sep).split(os.sep), v) for k, v in self.file_table.items() if k.startswith(dire)]
        tree_node = build_note_tree(dire, 0, notes)
        print_tree(tree_node)

    def print_relationships(self, fp):
        """Print relationships about a file.
        """
        fp = os.path.abspath(fp)
        for k, v in self.relation_table.items():
            if k.startswith(fp + sep):
                print(k, *v)
            elif k.endswith(sep + fp):
                print(k, *v)


def init_tables():
    """Init the data tables.
    """
    if not os.path.isdir(base_config.data.table_dir):
        os.makedirs(base_config.data.table_dir)
    # if not os.path.isfile(base_config.data.file_table_path):
    #     open(base_config.data.file_table_path, 'w', encoding='utf-8').write(f'path{sep}remark\n')
    # if not os.path.isfile(base_config.data.relation_table_path):
    #     open(base_config.data.relation_table_path, 'w', encoding='utf-8').write(f'path1{sep}path2{sep}relation\n')


# def read_tables():
#     """Read the exists data from tables."""
#     with open(base_config.data.file_table_path) as f:
#         f.readline()
#         file_data = f.readlines()
#         file_data = [line.strip().split(sep) for line in file_data]
#         file_table = {k: v for k, v in file_data}
#
#     relation_table = {}
#     return file_table, relation_table


def read_tables():
    """Read the existing data from tables."""
    file_table, relation_table = {}, {}
    if os.path.isfile(base_config.data.file_table_path):
        file_table = pickle.load(open(base_config.data.file_table_path, 'rb'))
    if os.path.isfile(base_config.data.relation_table_path):
        relation_table = pickle.load(open(base_config.data.relation_table_path, 'rb'))
    return file_table, relation_table


# def write_file_table(file_table):
#     """Write data to file_table."""
#     with open(base_config.data.file_table_path, 'w', encoding='utf-8') as f:
#         f.write(f'path{sep}remark\n')
#         for k, remark in file_table.items():
#             f.write(f'{k}{sep}{remark}\n')


# def add_remark(fp, remark, replace):
#     if fp in file_table:
#         if replace:
#             file_table[fp] = remark
#         else:
#             file_table[fp] = file_table[fp] + remark
#         write_file_table(file_table)
#     else:
#         with open(base_config.data.file_table_path, 'a', encoding='utf-8') as f:
#             f.write(f'{fp}{sep}{remark}\n')


# def add_note(fp, note, replace):
#     if fp in file_table:
#         if replace:
#             file_table[fp] = note
#             with open(base_config.data.file_table_path, 'wb') as f:
#                 pickle.dump(file_table, f)
#         else:
#             print(f"The file has been noted. If you want to replace it, use '-rp' in your command.")
#     else:
#         file_table[fp] = note
#         with open(base_config.data.file_table_path, 'wb') as f:
#             pickle.dump(file_table, f)


# def add_relation(fp1, fp2, relation, note, replace):
#     if not os.path.exists(fp1):
#         logging.error(f"{fp1} not exists.")
#         return
#     elif not os.path.exists(fp2):
#         logging.error(f"{fp2} not exists.")
#         return
#
#     fp1 = os.path.abspath(fp1)
#     fp2 = os.path.abspath(fp2)
#     key1 = fp1 + sep + fp2
#     key2 = fp2 + sep + fp1
#     if (key1 in relation_table or key2 in relation_table) and not replace:
#         logging.error(f"The relationship already exists. If you want to replace it, use '-rp' in your command.")
#         return
#     try:
#         relation = int(relation)
#     except ValueError:
#         logging.error(f"Unexpected relationship: {relation}")
#         return
#
#     if relation not in Relationship.__dict__['_value2member_map_']:
#         logging.error(f"Unexpected relationship: {relation}")
#         return
#
#     relation_table[key1] = (relation, note)
#     with open(base_config.data.relation_table_path, 'wb') as f:
#         pickle.dump(relation_table, f)


# def indices_of(lst: list, value):
#     indices = []
#     for i, val in enumerate(lst):
#         if val == value:
#             indices.append(i)
#     return indices


# def print_notes_recursively(dire):
#     """Print notes of files in the given directory recursively.
#     """
#     # filter out the notes the directory
#     dire = dire if dire else '/'
#     dire = os.path.abspath(dire)
#     notes = [(k.lstrip(dire).strip(os.sep).split(os.sep), v) for k, v in file_table.items() if k.startswith(dire)]
#     tree_node = build_note_tree(dire, 0, notes)
#     print_tree(tree_node)


def print_tree(node):
    if len(node.sons) == 0:
        file, layer, note = node.data
        print('   ' * (layer) + '|--', end='')
        formatted_print(file, note)
    else:
        file, layer = node.data[0], node.data[1]
        if layer > 0:
            print('   ' * (layer) + '|--', end='')
        print(file)
        for son in node.sons:
            print_tree(son)


def build_note_tree(dire, layer, notes):
    sub_dir2notes = {}
    sons = []
    for file, note in notes:
        if len(file) == 1:
            sons.append(FileTreeNode((file[0], layer + 1, note), []))
            continue

        if file[0] in sub_dir2notes:
            sub_dir2notes[file[0]].append((file[1:], note))
        else:
            sub_dir2notes[file[0]] = [(file[1:], note)]

    for sub_dir, rmk in sub_dir2notes.items():
        sons.append(build_note_tree(sub_dir, layer + 1, rmk))
    data = (dire, layer, '')
    root = FileTreeNode(data, sons)
    return root


def formatted_print(file, note):
    print(file, ':', note)


def filter_notes_by_keyword(file_table, kw):
    file_table = {k: v for k, v in file_table.items() if k.__contains__(kw) or v.__contains__(kw)}
    return file_table


# def print_relationships(fp):
#     """Print relationships about a file.
#     """
#     fp = os.path.abspath(fp)
#     for k, v in relation_table.items():
#         if k.startswith(fp + sep):
#             print(k, *v)
#         elif k.endswith(sep + fp):
#             print(k, *v)


if __name__ == '__main__':
    ...
    # base_config = parse_config('config.cfg')
    # sep = '\001\t'
    # init_tables()
    # file_table, relation_table = read_tables()
    #
    # parser = ArgumentParser(__name__)
    # parser.add_argument('--add', '-a', type=str, nargs='+', help='Add file note.')
    # parser.add_argument('--add_relation', '-ar', type=str, nargs='+', help='Add file note.')
    # parser.add_argument('--print_file', '-pf', action='store_true', help='Print the file table.')
    # parser.add_argument('--print_relation', '-pr', type=str, help='Print the relationships of a given file.')
    # parser.add_argument('--dir', '-d', type=str, help='Print the notes of files in the given dir.')
    # parser.add_argument('--keyword', '-k', type=str, help='Print the notes of files with the given keyword.')
    # parser.add_argument('--recursive', '-r', action='store_true', help='Print the notes of files in the given directory recursively.')
    # parser.add_argument('--replace', '-rp', action='store_true', help='If replace the existing note.')
    # args = parser.parse_args()
    #
    # if args.add:
    #     add = args.add
    #     assert len(add) == 2, 'The length of add must be 2.'
    #     fp, rmk = add
    #     if not os.path.exists(fp):
    #         raise FileNotFoundError(fp)
    #     else:
    #         fp = os.path.abspath(fp)
    #     add_note(fp, rmk, args.replace)
    #
    # if args.add_relation:
    #     add_rel = args.add_relation
    #     if len(add_rel) == 3:
    #         add_relation(*add_rel, '', replace=args.replace)
    #     elif len(add_rel) == 4:
    #         add_relation(*add_rel, replace=args.replace)
    #     else:
    #         logging.error('The length of add_relation must be 3 or 4.')
    #         sys.exit()
    #
    # if args.print_file:
    #     if args.keyword:
    #         file_table = filter_notes_by_keyword(file_table, args.keyword)
    #
    #     loc = os.path.abspath(args.dir) if args.dir else ''
    #     if not args.recursive:
    #         for k, v in file_table.items():
    #             if loc:
    #                 d = os.path.split(k)[0]
    #                 if d == loc:
    #                     formatted_print(k, v)
    #             else:
    #                 formatted_print(k, v)
    #     else:
    #         print_notes_recursively(args.dir)
    #
    # if args.print_relation:
    #     rel = args.print_relation
    #     print_relationships(rel)

