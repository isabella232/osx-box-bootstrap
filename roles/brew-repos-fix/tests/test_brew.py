def test_brew_installed(host):
    assert host.run_expect([0], 'source ~/.bash_profile && brew --help')

def test_brew_core_set_to_bitrise_io(host):
    git_config_file = _get_git_config_of_given_brew_repository(host, "core")

    assert git_config_file.exists
    assert git_config_file.contains('mirrors/github.com/bitrise-io/homebrew-core')

def test_brew_cask_set_to_bitrise_io(host):
    git_config_file = _get_git_config_of_given_brew_repository(host, "cask")

    assert git_config_file.exists
    assert git_config_file.contains('mirrors/github.com/bitrise-io/homebrew-cask')

def _get_git_config_of_given_brew_repository(host, repository):
    brew_repository = host.run('source ~/.bash_profile && brew --repository').stdout.strip()
    git_config_location = '{0}/Library/Taps/homebrew/homebrew-{1}/.git/config'.format(brew_repository, repository)

    return host.file(git_config_location)
