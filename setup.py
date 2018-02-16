import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.0.1"

include_files = ["datasets/verbs_2.csv"]
excludes = []
packages = ["os"]

setup(
    name = "SmuEsp",
    description='Simple console application for language learning',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("SmuEsp.py",base=None)]
)