# -*- coding: utf8 -*-
import pytest

from frigg_test_discovery import detect_test_tasks


@pytest.fixture
def files():
    return ['_config.yml', 'Cargo.toml', 'build.sbt', 'package.json', 'Gruntfile.js',
            'manage.py', 'setup.py', 'pom.xml', 'Rakefile', 'tox.ini', 'Makefile']


def test_detect_nothing(files):
    assert detect_test_tasks([]) == []
    assert detect_test_tasks(['random-file']) == []


def test_detect_make(files):
    assert detect_test_tasks(files) == ['make test']


def test_detect_tox(files):
    files = files[:len(files) - 1]
    assert detect_test_tasks(files) == ['tox']


def test_detect_rake(files):
    files = files[:len(files) - 2]
    assert detect_test_tasks(files) == ['rake test']


def test_detect_maven(files):
    files = files[:len(files) - 3]
    assert detect_test_tasks(files) == ['mvn -B test']


def test_detect_python(files):
    files = files[:len(files) - 4]
    assert detect_test_tasks(files) == ['python setup.py test']


def test_detect_django(files):
    files = files[:len(files) - 5]
    assert detect_test_tasks(files) == ['python manage.py test']


def test_detect_grunt(files):
    files = files[:len(files) - 6]
    assert detect_test_tasks(files) == ['grunt test']


def test_detect_npm(files):
    files = files[:len(files) - 7]
    assert detect_test_tasks(files) == ['npm install', 'npm test']


def test_detect_sbt(files):
    files = files[:len(files) - 8]
    assert detect_test_tasks(files) == ['sbt test']


def test_detect_cargo(files):
    files = files[:len(files) - 9]
    assert detect_test_tasks(files) == ['cargo test']


def test_detect_jekyll(files):
    files = files[:len(files) - 10]
    assert detect_test_tasks(files) == ['jekyll build']
