# -*- encoding: utf8 -*-
from setuptools import setup

import frigg_test_discovery


def _read_long_description():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst', format='markdown')
    except Exception:
        return None

version = frigg_test_discovery.__version__


setup(
    name='frigg-test-discovery',
    version=version,
    description='Test discovery util for frigg-worker',
    long_description=_read_long_description(),
    author='The frigg team',
    author_email='hi@frigg.io',
    license='MIT',
    url='https://github.com/frigg/frigg-test-discovery',
    py_modules=['frigg_test_discovery'],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
