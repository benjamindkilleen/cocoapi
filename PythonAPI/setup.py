from setuptools import setup, Extension
import numpy as np

import os

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

common_dir = '../common'
if os.path.exists('common'):
    common_dir = 'common'

sources = [os.path.join(common_dir, 'maskApi.c'), 'pycocotools/_mask.pyx']
include_dirs = [np.get_include(), common_dir]

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=sources,
        include_dirs=include_dirs,
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    ext_modules=ext_modules
)
