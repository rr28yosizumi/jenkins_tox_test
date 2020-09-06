#!/usr/bin/env python

"""Tests for `jenkins_tox_test` package."""


import unittest

from jenkins_tox_test import jenkins_tox_test


class TestJenkins_tox_test(unittest.TestCase):
    """Tests for `jenkins_tox_test` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        testlist = (
            '1.0',
            '123.0',
            '200',
            '10',
            '0',
            '0.12345678',
            '0.123456789',
            '123.123456789',
            '1234.123456789999999'
            )
        resultlist = (
            '1.00000000',
            '123.00000000',
            '200.00000000',
            '10.00000000',
            '0.00000000',
            '0.12345678',
            '0.12345678',
            '123.12345678',
            '1234.12345678'
        )
        result = [jenkins_tox_test.realnum_format(i) for i in testlist]

        self.assertListEqual(result,list(resultlist))

        testlist =(
            '0.1',
            '0.123',
            '0.1234',
            '0.12345',
            '0.123456',
            '0.1234567',
            '0.12345678',
            '0.123456789',
        )
        resultlist =(
            '0.10',
            '0.12',
            '0.12',
            '0.12',
            '0.12',
            '0.12',
            '0.12',
            '0.12',
        )
        result = [jenkins_tox_test.realnum_format(i,2) for i in testlist]

        self.assertListEqual(result,list(resultlist))

