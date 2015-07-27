# -*- coding: utf8 -*-
import logging

logger = logging.getLogger(__name__)

__version__ = '0.1.1'


def detect_test_tasks(files):
    if 'Makefile' in files:
        return ['make test']
    if 'tox.ini' in files:
        return ['tox']
    if 'setup.py' in files:
        return ['python setup.py test']
    if 'manage.py' in files:
        return ['python manage.py test']
    if 'package.json' in files:
        return ['npm install', 'npm test']
    if 'build.sbt' in files:
        return ['sbt test']
    if 'Cargo.toml' in files:
        return ['cargo test']
    if '_config.yml' in files:
        return ['jekyll build']
    return []
