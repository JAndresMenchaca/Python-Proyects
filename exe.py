from distutils.core import setup
import py2exe
import os
import getpass
import re
from random import randrange
from time import sleep
import sqlite3
from pathlib import Path

setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1}},
      console=["script.py"])
