import unittest
import os
import testinfra.utils.ansible_runner

class TestSSHSettings(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_host('anka-instance')

    def test_ssh_config_exists(self):
        home_path = "Users"
        param_user = "vagrant"
        ssh_config = self.host.file("/{}/{}/.ssh/config".format(home_path, param_user))

        self.assertTrue(ssh_config.exists)
        self.assertTrue(ssh_config.contains("StrictHostKeyChecking"))
        self.assertTrue(ssh_config.contains("UserKnownHostsFile"))

    def test_ssh_folder(self):
        home_path = "Users"
        param_user = "vagrant"
        ssh_config_folder = self.host.file("/{}/{}/.ssh".format(home_path, param_user))

        self.assertTrue(ssh_config_folder.is_directory)
        self.assertEqual(ssh_config_folder.user, param_user)
        self.assertEqual(ssh_config_folder.mode, 0o700)

if __name__ == '__main__':
    unittest.main()

