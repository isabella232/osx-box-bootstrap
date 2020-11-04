import unittest
import os
import testinfra.utils.ansible_runner

class TestBaseOS(unittest.TestCase):

    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_host('anka-instance')

    def test_autoupdates_are_disabled(self):
        self.assertEqual(self.host.run("sudo softwareupdate --schedule | grep -q 'off'").rc, 0)

    def test_spotlight_is_disabled(self):
        self.assertEqual(self.host.run("sudo launchctl list | grep -q com.apple.metadata.mds").rc, 0)

    def test_screenlock_is_disabled(self):
        self.assertIn("idleTime = 0;", self.host.run("sudo defaults -currentHost read com.apple.screensaver").stdout)

    def test_sleep_is_disabled(self):
        self.assertEqual(self.host.run("sudo systemsetup -getcomputersleep | grep -q Never").rc, 0)

    def test_screensaver_is_disabled(self):
        self.assertEqual(self.host.run('sudo defaults -currentHost read com.apple.screensaver | grep "idleTime = 0;"').rc, 0)
