import unittest
import os
import testinfra.utils.ansible_runner

class TestBaseXcode(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_host('instance')

    def test_profiles(self):
        users_home = '/Users/vagrant/'
        paths = ['.profiles/bitrise_profile', '.profiles/tools_profile', '.bashrc', '.zshrc', '.profile', '.bash_profile']

        for path in paths:
            self.assertTrue(self.host.file("{}{}".format(users_home, path)).is_file)

        self.assertTrue(self.host.file("{}.profiles".format(users_home)).is_directory)
        self.assertTrue(self.host.file("{}profile.d".format(users_home)).is_directory)

    def test_ruby(self):
        self.assertEqual(self.host.run('/Users/vagrant/.rbenv/shims/ruby --version').rc, 0)

    def test_brew(self):
        brew = self.host.run('/usr/local/bin/brew --version')
        self.assertEqual(brew.rc, 0)
        self.assertIn('Homebrew 2.5.8', brew.stdout)

    def test_xcode(self):
        xcode = self.host.run('/usr/bin/xcodebuild -version')
        self.assertEqual(xcode.rc, 0)
        self.assertIn('Xcode 12.1.1', xcode.stdout)
    
    def test_tmp_setup_basics(self):
        self.assertTrue(self.host.file('/Users/vagrant/Desktop/debug.log').is_file)
        with self.host.sudo():
            self.assertTrue(self.host.file('/etc/sudoers').contains('vagrant ALL=(ALL) NOPASSWD: ALL'))
            self.assertIn('Developer mode is already enabled.', self.host.run("DevToolsSecurity").stdout)
            self.assertIn('Automatic check is off', self.host.run("softwareupdate --schedule").stdout)
            self.assertEqual(self.host.run('launchctl list | grep com.apple.apsd.plist').rc, 1)
            self.assertIn('assessments disabled', self.host.run("spctl --status").stdout)

    def test_cmd_bridge_installed(self):
        self.assertEqual(self.host.run('/usr/local/bin/cmd-bridge --version').rc, 0)

