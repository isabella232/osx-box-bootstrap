def test_given_ruby_gems_are_installed(host):
    gems = ['pod', 'xcpretty', 'bundler', 'fastlane']
    for gem in gems:
      assert host.exists(gem)

def test_pod_versions(host):
    assert host.run("pod --version").stdout.startswith('1.10.0')
    assert host.run("xcpretty --version").stdout.startswith('0.3.0')
    assert host.run("bundler --version").stdout.startswith('Bundler version 2.1.4')
    assert host.run("gem list | grep fastlane | tail -1").stdout.startswith('fastlane (2.166.0')
