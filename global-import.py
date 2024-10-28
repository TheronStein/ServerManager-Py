import os
import sys

srcdir = os.path.join(os.environ['HOME'], 'servermanager-py')

# utils
menudir = os.path.join(srcdir, 'menus')
defdir = os.path.join(srcdir, 'utils', 'definitions')
funcdir = os.path.join(srcdir, 'utils', 'functions')
handir = os.path.join(srcdir, 'utils', 'handlers')
helpdir = os.path.join(srcdir, 'utils', 'helpers')

# misc
logdir = os.path.join(srcdir, 'logs')
tempdir = os.path.join(srcdir, 'temp')

# Add directories to sys.path for importing
sys.path.extend([menudir, defdir, funcdir, handir, helpdir])

# Import modules
import main
import screens

import configs
import files
import menus
import screens
import servers
import windows

import menuformat
import stringformat

import init
import boot_start
import hourly_check
import screens

import windows
import screens
import start
# import stop
import reset
import check