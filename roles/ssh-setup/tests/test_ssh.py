import unittest
import os
import testinfra.utils.ansible_runner

class TestSSHSettings(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_host('instance')
        self.vars = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_variables('instance')

    def test_ssh_config_exists(self):
        ssh_config = self.host.file("/{}/{}/.ssh/config".format(self.vars['param_user_home'], self.vars['param_user']))

        self.assertTrue(ssh_config.exists, "/{}/{}/.ssh/config".format(self.vars['param_user_home'], self.vars['param_user']))
        self.assertTrue(ssh_config.contains("StrictHostKeyChecking"))
        self.assertTrue(ssh_config.contains("UserKnownHostsFile"))

    def test_ssh_folder(self):
        ssh_config_folder = self.host.file("/{}/{}/.ssh".format(self.vars['param_user_home'], self.vars['param_user']))

        self.assertTrue(ssh_config_folder.is_directory)
        self.assertEqual(ssh_config_folder.user, self.vars['param_user'])
        self.assertEqual(ssh_config_folder.mode, 0o700)

if __name__ == '__main__':
    unittest.main()

