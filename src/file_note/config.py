# -*- coding: utf-8 -*-
"""
Description :
Authors     : lihp
CreateDate  : 2021/11/20
"""
import os
import configparser
from argparse import Namespace

sep = '\001\t'
table_dir = os.path.join(os.path.expanduser('~'), '.file_note')
file_table_path = os.path.join(table_dir, 'file_table.pkl')
relation_table_path = os.path.join(table_dir, 'relation_table.pkl')


def parse_config(config_path):
    """Parse configurations.
    Args:
        config_path: The path to a .cfg.
    """
    config_parser = configparser.ConfigParser()
    config_parser.read(config_path)
    config = dict2namespace(config_parser._sections)
    return config


def dict2namespace(dic):
    """Convert a `dict` to an `argparse.Namespace`.
    Args:
        dic: A `dict`.
    Returns:
        args: An instance of argparse.Namespace.
    """
    for k, v in dic.items():
        if isinstance(v, dict):
            v = dict2namespace(v)
            dic[k] = v
    return Namespace(**dic)


def parse_config_test():
    config = parse_config('config.cfg')
    print(config)


if __name__ == '__main__':
    ...
    parse_config_test()
