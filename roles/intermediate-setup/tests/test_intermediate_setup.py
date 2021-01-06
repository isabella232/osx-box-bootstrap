import unittest
import os
import platform
import testinfra.utils.ansible_runner
from ddt import ddt, data


@ddt
class TestIntermediateSetup(unittest.TestCase):
    user_home = "/home/linuxbrew" if platform.system() != 'darwin' else '/Users/vagrant/'

    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']).get_host('instance')

    @data(
        'ansible',
        'flow',
        'gdate',
        'git',
        'gs',
        'hg',
        'magick',
        'python3',
        'screen',
        'tree',
        'watchman',
        'wget',
        'yarn')
    def test_brew_packages_exist(self, package):
        self.assertTrue(self.host.exists(package))

    def test_firebase_cli_exists(self):
        self.assertTrue(self.host.exists("firebase"))

    @data(
        "{}/bin".format(user_home),
        "{}/bitrise".format(user_home),
        "{}/bitrise/stepdata".format(user_home),
        "{}/bitrise/tools".format(user_home),
        "{}/build".format(user_home),
        "{}/deploy".format(user_home),
        "{}/git".format(user_home),
        "{}/profiles".format(user_home),
        "{}/stepdir".format(user_home),
        "Library/MobileDevice/Provisioning Profiles")
    def test_bitrise_specific_folder(self, dir):
        self.assertTrue(self.host.file(dir).exists, dir)

    def test_pip_exists(self):
        self.assertTrue(self.host.exists("pip3"))
