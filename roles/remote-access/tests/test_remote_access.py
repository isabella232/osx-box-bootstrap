# Remote access scripts
def test_bitrise_folder_exists(host):
    bitrise = host.file("/opt/bitrise")
    assert bitrise.user == "linuxbrew"
    assert bitrise.group == "wheel"
    assert bitrise.mode == 0o755

def test_ngrok_exists(host):
    ngrok = host.file("/etc/ngrok")
    assert ngrok.user == "root"
    assert ngrok.group == "wheel"
    assert ngrok.mode == 0o755

def test_bootstrap_script_exists(host):
    bootstrap_script = host.file("/opt/bitrise/bootstrap_remote_access.sh.tmpl")
    assert bootstrap_script.user == "linuxbrew"
    assert bootstrap_script.mode == 0o777

# Test ngrok
def test_ngrok_exists(host):
    assert host.exists("ngrok")
    nkgrok_bin = host.file("/usr/local/bin/ngrok")
    assert nkgrok_bin.mode == 0o700
