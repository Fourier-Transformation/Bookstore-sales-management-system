"""
Load Configrations from ini file
"""

import configparser as _configparser

def load(path, section):
    """
    load configrations by specifying config file path and the section
    """
    parser = _configparser.ConfigParser()
    parser.read(path, encoding='utf-8')

    return tuple(dict(parser.items(section)).values())
    