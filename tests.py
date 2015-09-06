# -*- coding: utf8 -*-
import pytest

from frigg_test_discovery import detect_test_tasks


@pytest.fixture
def files():
    return ['_config.yml', 'Cargo.toml', 'build.sbt', 'package.json', 'gulpfile.js', 'Gruntfile.js',
            'manage.py', 'setup.py', 'pom.xml', 'Rakefile', 'tox.ini', 'Makefile']


def test_detect_nothing(files):
    assert detect_test_tasks([]) == []
    assert detect_test_tasks(['random-file']) == []


def test_detect_make(files):
    assert detect_test_tasks(files) == ['make test']


def test_detect_tox(files):
    files = files[:files.index('tox.ini') + 1]
    assert detect_test_tasks(files) == ['tox']


def test_detect_rake(files):
    files = files[:files.index('Rakefile') + 1]
    assert detect_test_tasks(files) == ['rake test']


def test_detect_maven(files):
    files = files[:files.index('pom.xml') + 1]
    assert detect_test_tasks(files) == ['mvn -B test']


def test_detect_python(files):
    files = files[:files.index('setup.py') + 1]
    assert detect_test_tasks(files) == ['python setup.py test']


def test_detect_django(files):
    files = files[:files.index('manage.py') + 1]
    assert detect_test_tasks(files) == ['python manage.py test']


def test_detect_grunt(files):
    files = files[:files.index('Gruntfile.js') + 1]
    assert detect_test_tasks(files) == ['grunt test']


def test_detect_gulp(files):
    files = files[:files.index('gulpfile.js') + 1]
    assert detect_test_tasks(files) == ['gulp test']


def test_detect_npm(files):
    files = files[:files.index('package.json') + 1]
    assert detect_test_tasks(files) == ['npm install', 'npm test']


def test_detect_sbt(files):
    files = files[:files.index('build.sbt') + 1]
    assert detect_test_tasks(files) == ['sbt test']


def test_detect_cargo(files):
    files = files[:files.index('Cargo.toml') + 1]
    assert detect_test_tasks(files) == ['cargo test']


def test_detect_jekyll(files):
    files = files[:files.index('_config.yml') + 1]
    assert detect_test_tasks(files) == ['jekyll build']
