import unittest
import os
import testinfra.utils.ansible_runner

class TestSSHDConfig(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_host('instance')
        self.vars = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_variables('instance')

    def test_sshd_config_exists(self):
        self.assertTrue(self.host.file("/etc/ssh/sshd_config").exists)

    def test_sshd_config_is_valid(self):
        self.assertTrue(self.host.run("/usr/sbin/sshd -t -f /etc/ssh/sshd_config").succeeded)

    def test_sshd_config_permissions(self):
        sshd_config = self.host.file("/etc/ssh/sshd_config")
        self.assertEqual(sshd_config.user, 'root')
        self.assertEqual(sshd_config.group, 'root')
        self.assertEqual(sshd_config.mode, 0o644)

    def test_sshd_config_content(self):
        sshd_config = self.host.file("/etc/ssh/sshd_config")
        self.assertTrue(sshd_config.contains("Ansible managed"))
        self.assertTrue(sshd_config.contains("bitrise overrides"))
        self.assertRegex(sshd_config.content_string, r'LogLevel\s+VERBOSE')


if __name__ == '__main__':
    unittest.main()

