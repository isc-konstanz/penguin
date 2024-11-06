#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
penguin
~~~~~~~

To learn how to use local resource integration systems, see "penguin --help"

"""

import os
from argparse import ArgumentParser, RawTextHelpFormatter

import penguin

os.environ["NUMEXPR_MAX_THREADS"] = str(os.cpu_count())


def _get_parser() -> ArgumentParser:
    from penguin import __version__

    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s {version}".format(version=__version__))

    return parser


if __name__ == "__main__":
    with penguin.load(parser=_get_parser()) as application:
        application.main()
