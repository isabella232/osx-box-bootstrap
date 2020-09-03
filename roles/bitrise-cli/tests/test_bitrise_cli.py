def test_bitrise_cli_exists(host):
    bitrise_cli = host.file("/usr/local/bin/bitrise")
    assert bitrise_cli.user == "linuxbrew"
    assert bitrise_cli.group == "wheel"
    assert bitrise_cli.mode == 0o755

def test_bitrise_cli_version(host):
    assert host.run("bitrise --version").stdout.startswith('1.42.0')

def test_envman_is_installed(host):
    assert host.exists("/home/linuxbrew/.bitrise/tools/envman")

def test_stepman_is_installed(host):
    assert host.exists("/home/linuxbrew/.bitrise/tools/stepman")