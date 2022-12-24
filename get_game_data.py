import imp
import os
import json
import shutil
from subprocess import PIPE
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass souece and target directory only")