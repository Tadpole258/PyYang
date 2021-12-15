# --------------------------------------------------------
# Python Projects for Study or Work
# Copyright (c) 2021 NiceGroup.....
# Licensed under Yang..............
# Written by Yang..................
# --------------------------------------------------------

import os.path as op
import configparser

# file abspath
file_abspath = op.abspath(__file__)
# folder path
dir_path = op.dirname(file_abspath)


# *******************
# config.ini
# *******************
parser = configparser.ConfigParser()
# read config.ini information
parser.read(op.join(dir_path, 'config.ini'))
# signal = dict(parser.items('NiceJstDB'))
database = dict(parser.items('NiceYqDB'))

