def test_flutter_properly_installed(host):
    assert "Flutter 1.20.3" in host.run("/usr/local/flutter/bin/flutter --version").stdout
