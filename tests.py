# -*- coding: utf8 -*-
import unittest

from frigg_test_discovery import detect_test_tasks


class DetectTestRunnerTests(unittest.TestCase):
    def setUp(self):
        self.files = ['_config.yml', 'Cargo.toml', 'build.sbt', 'package.json', 'Gruntfile.js',
                      'manage.py', 'setup.py', 'pom.xml', 'Rakefile', 'tox.ini', 'Makefile']

    def test_detect_nothing(self):
        self.assertEqual(detect_test_tasks([]), [])
        self.assertEqual(detect_test_tasks(['random-file']), [])

    def test_detect_make(self):
        self.assertEqual(detect_test_tasks(self.files), ['make test'])

    def test_detect_tox(self):
        self.files = self.files[:len(self.files) - 1]
        self.assertEqual(detect_test_tasks(self.files), ['tox'])

    def test_detect_rake(self):
        self.files = self.files[:len(self.files) - 2]
        self.assertEqual(detect_test_tasks(self.files), ['rake test'])

    def test_detect_maven(self):
        self.files = self.files[:len(self.files) - 3]
        self.assertEqual(detect_test_tasks(self.files), ['mvn -B test'])

    def test_detect_python(self):
        self.files = self.files[:len(self.files) - 4]
        self.assertEqual(detect_test_tasks(self.files), ['python setup.py test'])

    def test_detect_django(self):
        self.files = self.files[:len(self.files) - 5]
        self.assertEqual(detect_test_tasks(self.files), ['python manage.py test'])

    def test_detect_grunt(self):
        self.files = self.files[:len(self.files) - 6]
        self.assertEqual(detect_test_tasks(self.files), ['grunt test'])

    def test_detect_npm(self):
        self.files = self.files[:len(self.files) - 7]
        self.assertEqual(detect_test_tasks(self.files), ['npm install', 'npm test'])

    def test_detect_sbt(self):
        self.files = self.files[:len(self.files) - 8]
        self.assertEqual(detect_test_tasks(self.files), ['sbt test'])

    def test_detect_cargo(self):
        self.files = self.files[:len(self.files) - 9]
        self.assertEqual(detect_test_tasks(self.files), ['cargo test'])

    def test_detect_jekyll(self):
        self.files = self.files[:len(self.files) - 10]
        self.assertEqual(detect_test_tasks(self.files), ['jekyll build'])
