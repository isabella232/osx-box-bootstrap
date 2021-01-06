import unittest
import os
import testinfra.utils.ansible_runner

class TestBrewFixes(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_host('instance')

    def test_brew_installed(self):
        self.assertTrue(self.host.run_expect([0], 'source ~/.bash_profile && brew --help'))

    def test_brew_core_set_to_bitrise_io(self):
        git_config_file = self._get_git_config_of_given_brew_repository("core")

        self.assertTrue(git_config_file.exists)
        self.assertTrue(git_config_file.contains('mirrors/github.com/bitrise-io/homebrew-core'))

    def test_brew_cask_set_to_bitrise_io(self):
        git_config_file = self._get_git_config_of_given_brew_repository("cask")

        self.assertTrue(git_config_file.exists)
        self.assertTrue(git_config_file.contains('mirrors/github.com/bitrise-io/homebrew-cask'))

    def _get_git_config_of_given_brew_repository(self, repository):
        brew_repository = self.host.run('source ~/.bash_profile && brew --repository').stdout.strip()
        git_config_location = '{0}/Library/Taps/homebrew/homebrew-{1}/.git/config'.format(brew_repository, repository)

        return self.host.file(git_config_location)
