import unittest
import os
import testinfra.utils.ansible_runner


class TestIntermediateSetup(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']).get_host('instance')

    def test_cmd_bridge_file_related_settings(self):
        self.assertTrue(self.host.file("/Users/vagrant/Library/LaunchAgents/").exists, "LaunchAgents directory does not exists for cmd-bridge")
        self.assertTrue(self.host.file("/Users/vagrant/Library/LaunchAgents/bitrise.io.tools.cmd-bridge.plist").exists, "bitrise.io.tools.cmd-bridge.plist is not at the correct place")
        self.assertTrue(self.host.file("/Users/vagrant/logs").exists, "Log directory for cmd-bridge has not been created")

    def test_cmd_bridge_is_runnins(self):
        self.assertEqual(self.host.run("ps aux | grep cmd-bridge").rc, 0)

    def test_cmd_bridge_is_using_the_correct_log_files(self):
        cmd_bridge_log = self.host.file("/Users/vagrant/logs/bitrise.io.tools.cmd-bridge.log")
        self.assertTrue(cmd_bridge_log.exists)
        self.assertEqual(cmd_bridge_log.content_string.count("Ready to serve on port"), 1)
