import unittest
import os
import testinfra.utils.ansible_runner
from ddt import ddt, data


@ddt
class TestBaseStack(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']).get_host('anka-instance')

    @data(
        'go version',
        'python --version',
        'node --version',
        'npm --version',
        'yarn --version',
        'java -version',
        'git --version',
        'git lfs version',
        'hg --version',
        'curl --version',
        'wget --version',
        'rsync --version',
        'unzip -v',
        'zip -v',
        'tar --version',
        'tree --version',
        'brew --version',
        'ansible --version',
        'gtimeout --version',
        'watchman --version',
        'flow version',
        'carthage version',
        'convert --version',
        'ps2ascii --version',
        'screen --version',
        'firebase --version',
        'applesimutils -v',
        'jq --version',
        'xcbeautify --version',
        'xclogparser version',
        'screen --version',
        'applesimutils --version',
        'openconnect --version',
        'ruby --version')
    def test_installed_system_tools(self, tool):
        self.assertEqual(self.host.run(tool).rc, 0, tool)

    @data(
        'bitrise --version',
        '/Users/vagrant/.bitrise/tools/stepman --version',
        '/Users/vagrant/.bitrise/tools/envman --version',
        'cmd-bridge --version')
    def test_bitrise_tools(self, tool):
        self.assertEqual(self.host.run(tool).rc, 0, tool)

    @data(
        'cordova --version',
        'ionic --version',
        'appcenter --version')
    def test_npm_packages_version(self, tool):
        self.assertEqual(self.host.run(tool).rc, 0, tool)

    @data(
        'xcode-select --print-path',
        'xcodebuild -version',
        'swift --version',
        'xcrun simctl list')
    def test_xcode_related_packages(self, tool):
        self.assertEqual(self.host.run(tool).rc, 0, tool)
