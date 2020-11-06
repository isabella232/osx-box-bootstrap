def test_bitrise_den_agent(host):
    bitrise_cli = host.file("/Users/vagrant/bitrise-den-agent")
    assert bitrise_cli.user == "linuxbrew"
    assert bitrise_cli.group == "staff"
    assert bitrise_cli.mode == 0o755
