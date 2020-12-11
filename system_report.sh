#!/bin/bash
set -e

if [[ "${IS_IGNORE_ERRORS}" == "true" ]] ; then
echo " (i) Ignore Errors: enabled"
set +e
else
echo " (i) Ignore Errors: disabled"
fi

echo
echo '#'
echo '# This System Report was generated by: https://github.com/bitrise-io/osx-box-bootstrap/blob/master/system_report.sh'
echo '#  Pull Requests are welcome!'
echo '#'
echo

echo
echo "=== Revision / ID ======================"
echo "* BITRISE_OSX_STACK_REV_ID: $BITRISE_OSX_STACK_REV_ID"
echo "========================================"
echo
# Make sure that the reported version is only
#  a single line!
echo
echo "=== Pre-installed tool versions ========"

ver_line="$(go version)" ;                        echo "* Go: $ver_line"
ver_line="$(python --version 2>&1 >/dev/null)" ;  echo "* Python: $ver_line"
ver_line="$(node --version)" ;                    echo "* Node.js: $ver_line"
ver_line="$(npm --version)" ;                     echo "* NPM: $ver_line"
ver_line="$(yarn --version)" ;                    echo "* Yarn: $ver_line"
ver_line="$(java -version 2>&1 >/dev/null)" ;     echo "* Java: $ver_line"
# This is needed because Flutter version displays a message on the first try
# that new updates are available, and only displays the actual version afterwards
# When we run it again it displays the current version only
flutter --version > /dev/null 2>&1
ver_line="$(flutter --version | head -n 1)" ;     echo "* Flutter: $ver_line"

echo
ver_line="$(git --version)" ;                     echo "* git: $ver_line"
ver_line="$(git lfs version)" ;                   echo "* git lfs: $ver_line"
ver_line="$(hg --version | grep version)" ;       echo "* mercurial/hg: $ver_line"
ver_line="$(curl --version | grep curl)" ;        echo "* curl: $ver_line"
ver_line="$(wget --version | grep 'GNU Wget')" ;  echo "* wget: $ver_line"
ver_line="$(rsync --version | grep version)" ;    echo "* rsync: $ver_line"
ver_line="$(unzip -v | head -n 1)" ;              echo "* unzip: $ver_line"
ver_line="$(zip -v | head -n 2 | tail -n 1)";     echo "* zip: $ver_line"
ver_line="$(tar --version | head -n 1)" ;         echo "* tar: $ver_line"
ver_line="$(tree --version)" ;                    echo "* tree: $ver_line"

echo
ver_line="$(brew --version)" ;                    echo "* brew: $ver_line"




ver_line="$(ansible --version | grep ansible)" ;              echo "* Ansible: $ver_line"
ver_line="$(gtimeout --version | grep 'timeout')" ;           echo "* gtimeout: $ver_line"
ver_line="$(watchman --version)" ;                            echo "* watchman: $ver_line"
ver_line="$(flow version)" ;                                  echo "* flow: $ver_line"
ver_line="$(carthage version)" ;                              echo "* carthage: $ver_line"
ver_line="$(convert --version | head -1)" ;                   echo "* imagemagick (convert): $ver_line"
ver_line="$(ps2ascii --version)" ;                            echo "* ghostscript (ps2ascii): $ver_line"
ver_line="$(screen --version | grep Screen)" ;                echo "* screen: $ver_line"
ver_line="$(firebase --version)" ;                            echo "* firebase: $ver_line"
ver_line="$(applesimutils -v)" ;                              echo "* $ver_line"
ver_line="$(jq --version | sed 's/.*\(...\)/\1/')";           echo "* jq: $ver_line"
ver_line="$(xcbeautify --version)";                           echo "* $ver_line"
ver_line="$(xclogparser version)";                            echo "* $ver_line"
ver_line="$(screen --version | awk '{print $1, $3}')";        echo "* $ver_line"
ver_line="$(applesimutils --version | awk '{print $1, $3}')"; echo "* $ver_line"
ver_line="$(openconnect --version | head -n 1)";              echo "* $ver_line"
ver_line="$(aws --version)" ;                                 echo "* aws-cli: $ver_line"




echo
echo "--- Bitrise CLI tool versions"
ver_line="$(bitrise --version)" ;                 echo "* bitrise: $ver_line"
ver_line="$(/Users/vagrant/.bitrise/tools/stepman --version)" ; echo "* stepman: $ver_line"
ver_line="$(/Users/vagrant/.bitrise/tools/envman --version)" ;  echo "* envman: $ver_line"
ver_line="$(cmd-bridge --version)" ;              echo "* cmd-bridge: $ver_line"
echo "========================================"
echo

echo
echo "=== Brew list versions =================="
brew list --versions
echo "========================================"
echo

echo
echo "=== Brew deps tree =================="
brew deps --tree --installed
echo "========================================"
echo

echo
echo "=== Ruby and rubygems =================="

if [ -x "$(command -v rbenv)" ] ; then
  ver_line="$(ruby --version)" ;                  echo "* Ruby (default): $ver_line"
  echo "--- Available ruby versions ---"
  rbenv versions
  echo "-------------------------------"
  ver_line="$(rbenv --version | cut -d ' ' -f 2)" ; echo "* rbenv: $ver_line"
else
  ver_line="$(ruby --version)" ;                  echo "* Ruby: $ver_line"
fi
ver_line="$(gem --version)" ;                     echo "* Rubygems: $ver_line"
ver_line="$(bundle --version)" ;                  echo "* Bundler: $ver_line"
ver_line="$(pod --version)" ;                     echo "* CocoaPods: $ver_line"
ver_line="$(xcpretty --version)" ;                echo "* xcpretty: $ver_line"
echo "========================================"
echo

echo
echo "=== All Ruby GEMs ======================"
gem list
echo "========================================"
echo

echo
echo "=== NPM global packages =========================="
ver_line="$(cordova --version)" ;                       echo "* Cordova: $ver_line"
ver_line="$(ionic --version)" ;                         echo "* Ionic: $ver_line"
ver_line="$(appcenter --version | awk '{print $3}')" ;  echo "* Appcenter-CLI version: $ver_line"
echo "========================================"
echo

echo
echo "=== Checking Xcode CLT dirs ============"
# installed by `xcode-select --install`, if called *before*
#  Xcode.app is installed
echo
if [[ -d /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include/CommonCrypto ]]
then
    echo " * ls -1 /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include/CommonCrypto"
    ls -1 /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include/CommonCrypto
elif [[ -d /usr/include/CommonCrypto ]]
then
    echo " * ls -1 /usr/include/CommonCrypto"
    ls -1 /usr/include/CommonCrypto
elif [[ -d /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/CommonCrypto ]]
then
    echo " ls -1 /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/CommonCrypto"
    ls -1 /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/CommonCrypto
fi
echo
echo " * ls -1 /Library/Developer/CommandLineTools/"
ls -1 /Library/Developer/CommandLineTools/
echo
echo " * /Library/Developer/CommandLineTools/usr/bin/swift --version"
/Library/Developer/CommandLineTools/usr/bin/swift --version
echo
echo "========================================"
echo

echo
echo "=== Xcode =============================="
echo
echo "* Active Xcode Command Line Tools:"
xcode-select --print-path
echo
echo "* Xcode Version:"
xcodebuild -version
echo
echo "* /usr/bin/swift --version"
/usr/bin/swift --version
echo
echo "* Installed SDKs:"
xcodebuild -showsdks
echo
echo "* Available Simulators:"
xcrun simctl list | grep -i --invert-match 'unavailable'
echo
echo "========================================"
echo

echo
echo "=== OS X info ========================="
echo
echo "* sw_vers"
sw_vers
echo
echo "* system_profiler SPSoftwareDataType"
system_profiler SPSoftwareDataType
echo
echo "========================================"
echo

echo
echo "=== System infos ======================="
info_line="$( df -gh / | awk '{printf "%14s %12s %12s\n", $1, $2, $4}' )" ;
echo "* Free disk space:
$info_line"
echo "========================================"
echo

if [ ! -z "$BITRISE_XAMARIN_FOLDER_PATH" ] ; then
  echo
  echo "=== Xamarin specific ==================="
  echo
  echo "--- Xamarin"
  echo
  if [ -e "/Applications/Visual Studio.app/Contents/Resources/lib/monodevelop/bin/buildinfo" ] ; then
    echo "* Visual Studio"
    cat "/Applications/Visual Studio.app/Contents/Resources/lib/monodevelop/bin/buildinfo"
  else
    echo "* Xamarin Studio"
    cat "/Applications/Xamarin Studio.app/Contents/Resources/lib/monodevelop/bin/buildinfo"
  fi
  echo
  echo "* Mono version:"
  mono --version
  echo "* Mono path:"
  which mono
  echo
  echo "* Xamarin.Android"
  ls /Library/Frameworks/Xamarin.Android.framework/Versions
  echo
  echo "* Xamarin.iOS"
  ls /Library/Frameworks/Xamarin.iOS.framework/Versions
  echo
  echo "* debug.keystore path:"
  debug_keystore_pth="$HOME/.local/share/Xamarin/Mono for Android/debug.keystore"
  if [ -f "${debug_keystore_pth}" ] ; then
    echo "$debug_keystore_pth"
  else
    echo "Missing android debug.keystore"
    if [[ "$BITRISE_OSX_STACK_REV_ID" != "v2016_08_10_1" ]] ; then
      # Fail, unless old LTS Xamarin stack
      tree "$HOME/.local/share"
      exit 1
    fi
  fi
fi

if [ -n "$ANDROID_HOME" ] ; then
  echo "--- Android"
  echo
  echo "* ANDROID_HOME (${ANDROID_HOME}) content:"
  ls -1 ${ANDROID_HOME}
  echo
  echo "* ANDROID_NDK_HOME (${ANDROID_NDK_HOME}) content:"
  if [ -z "$ANDROID_NDK_HOME" ] ; then
    if [[ "$BITRISE_OSX_STACK_REV_ID" == "v2016_08_10_1" ]] ; then
      # Old, LTS Xamarin stack
      echo " (!) ANDROID_NDK_HOME environment variable is not defined!"
    else
      echo " [!] ANDROID_NDK_HOME environment variable is not defined!"
      exit 1
    fi
  else
    ls -1 ${ANDROID_NDK_HOME}

    echo
    echo "* Android NDK Version:"
    cat "${ANDROID_NDK_HOME}/source.properties"
  fi
  echo
  echo "* platform-tools content:"
  ls -1 ${ANDROID_HOME}/platform-tools
  echo
  echo "* build-tools content:"
  ls -1 ${ANDROID_HOME}/build-tools
  echo
  echo "* extras content:"
  tree -L 2 ${ANDROID_HOME}/extras
  echo
  echo "* platforms content:"
  ls -1 ${ANDROID_HOME}/platforms
  echo
  echo "* system-images content:"
  tree -L 3 ${ANDROID_HOME}/system-images
  echo
  echo "========================================"
  echo
fi

echo
echo "=== Android APK tools =================="
echo
echo "* aapt2:"
/opt/apktools/aapt2 version
echo
echo "========================================"
echo

echo
echo "=== Environment infos ======================="
if [ -z "${MATCH_KEYCHAIN_PASSWORD}" ] ; then
  echo "MATCH_KEYCHAIN_PASSWORD environment NOT set"
  exit 1
else
  echo "MATCH_KEYCHAIN_PASSWORD environment set"
fi
echo "========================================"
echo

echo
echo "=== Control tests ======================"
# these things should pass;
# e.g. testing the existence of specific paths
# or whether ~/.bash_profile can be "source"-d in "set -e" mode
set -e
echo 'source $HOME/.bash_profile ...'
source $HOME/.bash_profile
echo 'source $HOME/.bash_profile - PASSED'
echo "========================================"
echo
