import unittest
import os
import testinfra.utils.ansible_runner
from ddt import ddt, data


@ddt
class TestIntermediateSetup(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']).get_host('anka-instance')

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

    def test_ansible_cfg_exists(self):
        ansible_cfg = self.host.file("/Users/vagrant/ansible.cfg")
        self.assertEqual(ansible_cfg.user, 'vagrant')

    def test_firebase_cli_exists(self):
        self.assertTrue(self.host.exists("firebase"))

    @data(
        "/Users/vagrant/bin",
        "/Users/vagrant/bitrise",
        "/Users/vagrant/bitrise/stepdata",
        "/Users/vagrant/bitrise/tools",
        "/Users/vagrant/build",
        "/Users/vagrant/deploy",
        "/Users/vagrant/git",
        "/Users/vagrant/profiles",
        "/Users/vagrant/stepdir",
        "Library/MobileDevice/Provisioning Profiles")
    def test_bitrise_specific_folder(self, dir):
        self.assertTrue(self.host.file(dir).exists)

    def test_pip_exists(self):
        self.assertTrue(self.host.exists("pip3"))
