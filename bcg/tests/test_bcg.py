import bcg

import os

from unittest import TestCase, mock


class GetTypesDirsTests(TestCase):
    def test_get_types_dirs__no_xdg_no_home(self):
        expected = [os.path.join(os.path.dirname(bcg.__file__), 'types')]
        with mock.patch.dict('os.environ', {}, clear=True):
            actual = bcg.get_types_dirs()
        self.assertEqual(expected, actual)

    def test_get_types_dirs__no_xdg(self):
        expected = [
            'foo/.config/bcg/types',
            os.path.join(os.path.dirname(bcg.__file__), 'types')
        ]
        with mock.patch.dict('os.environ', {'HOME': 'foo'}, clear=True):
            actual = bcg.get_types_dirs()
        self.assertEqual(expected, actual)

    def test_get_types_dirs__all_vars_one_config_dirs(self):
        expected = [
            'foo/bcg/types',
            'xdg_home_config/bcg/types',
            os.path.join(os.path.dirname(bcg.__file__), 'types'),
        ]
        env_vars = {
            'HOME': 'baz',
            'XDG_CONFIG_DIRS': 'foo',
            'XDG_CONFIG_HOME': 'xdg_home_config'
        }
        with mock.patch.dict('os.environ', env_vars, clear=True):
            actual = bcg.get_types_dirs()
        self.assertEqual(expected, actual)

    def test_get_types_dirs__all_vars_multiple_config_dirs(self):
        expected = [
            'foo/bcg/types',
            'bar/bcg/types',
            'xdg_home_config/bcg/types',
            os.path.join(os.path.dirname(bcg.__file__), 'types'),
        ]
        env_vars = {
            'HOME': 'baz',
            'XDG_CONFIG_DIRS': 'foo:bar',
            'XDG_CONFIG_HOME': 'xdg_home_config'
        }
        with mock.patch.dict('os.environ', env_vars, clear=True):
            actual = bcg.get_types_dirs()
        self.assertEqual(expected, actual)
