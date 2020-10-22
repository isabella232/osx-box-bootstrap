import testinfra

# Test if autoupdates are disabled
def test_autoupdates_are_disabled(host):
    assert host.run("sudo softwareupdate --schedule | grep -q 'off'").rc == 0

# Test if spotlight is disabled
def test_spotlight_is_disabled(host):
    assert host.run("sudo launchctl list | grep -q com.apple.metadata.mds").rc == 0

# Test is sleep mode is disabled
def test_screenlock_is_disabled(host):
    assert "idleTime = 0;" in host.run("sudo defaults -currentHost read com.apple.screensaver").stdout

# Test if display sleep is disabled
def test_sleep_is_disabled(host):
    assert host.run("sudo systemsetup -getcomputersleep | grep -q Never").rc == 0

# Test if screensaver is disabled
def test_screensaver_is_disabled(host):
    assert host.run('sudo defaults -currentHost read com.apple.screensaver | grep "idleTime = 0;"').rc == 0
