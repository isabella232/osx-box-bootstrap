import unittest
import os
import testinfra.utils.ansible_runner


class TestIntermediateSetup(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']).get_host('anka-instance')

    def test_cmd_bridge_file_related_settings(self):
        self.assertTrue(self.host.file("/Users/vagrant/Library/LaunchAgents/").exists, "LaunchAgents directory does not exists for cmd-bridge")
        self.assertTrue(self.host.file("/Users/vagrant/Library/LaunchAgents/bitrise.io.tools.cmd-bridge.plist").exists, "bitrise.io.tools.cmd-bridge.plist is not at the correct place")
        self.assertTrue(self.host.file("/Users/vagrant/logs").exists, "Log directory for cmd-bridge has not been created")
