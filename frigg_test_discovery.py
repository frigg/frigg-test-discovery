# -*- coding: utf8 -*-
import logging

logger = logging.getLogger(__name__)

__version__ = '1.4.1'


def detect_test_tasks(files):
    if 'Makefile' in files:
        return ['make test']
    if 'tox.ini' in files:
        return ['tox']
    if 'Rakefile' in files:
        return ['rake test']
    if 'pom.xml' in files:
        return ['mvn -B test']
    if 'setup.py' in files:
        return ['python setup.py test']
    if 'manage.py' in files:
        return ['python manage.py test']
    if 'Gruntfile.js' in files:
        return['grunt test']
    if 'gulpfile.js' in files:
        return['gulp test']
    if 'package.json' in files:
        return ['npm install', 'npm test']
    if 'build.sbt' in files:
        return ['sbt test']
    if 'Cargo.toml' in files:
        return ['cargo test']
    if '_config.yml' in files:
        return ['jekyll build']
    return []


def detect_tox_environments(runner, working_directory):
    result = runner.run('tox -l', working_directory)
    return result.out.split()
