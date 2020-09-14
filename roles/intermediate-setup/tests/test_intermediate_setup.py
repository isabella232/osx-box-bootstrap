def test_brew_packages_exist(host):
    packages = ['ansible','flow','gdate','git','gs','hg','magick','python3','screen','tree','watchman','wget','yarn']
    for package in packages:
      assert host.exists(package)

def test_ansible_cfg_exists(host):
    ansible_cfg = host.file("/home/linuxbrew/ansible.cfg" )
    assert ansible_cfg.user == "linuxbrew"

def test_firebase_cli_exists(host):
    assert host.exists("firebase")

def test_bitrise_specific_folder(host):
    folders = [
        "/home/linuxbrew/bin",
        "/home/linuxbrew/bitrise",
        "/home/linuxbrew/bitrise/stepdata",
        "/home/linuxbrew/bitrise/tools",
        "/home/linuxbrew/build",
        "/home/linuxbrew/deploy",
        "/home/linuxbrew/git",
        "/home/linuxbrew/profiles",
        "Library/MobileDevice/Provisioning Profiles",
        "/home/linuxbrew/stepdir"
    ]
    for folder in folders:
        assert host.file(folder).exists

def test_pip_exists(host):
    assert host.exists("pip3")
