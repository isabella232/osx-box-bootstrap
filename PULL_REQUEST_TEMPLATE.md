### New Pull Request Checklist

*Please mark the points which you did / accept.*

- [ ] The tool I added is stable, and __does not require frequent updates__. _Preinstalled tools on the LTS stacks
  are not updated, so if the tool requires frequent updates you should handle the installation on-demand (see: [Install Any Additional Tool - DevCenter](https://bitrise-io.github.io/devcenter/tips-and-tricks/install-additional-tools/) for more information)_
- [ ] I updated the corresponding tests if there were any.
- [ ] I added a version report line to [`system_report.sh`](/system_report.sh) for the new tool(s) I added
- [ ] I have added an entry to the CHANGELOG.md with a revisionID (the current date and the number of the change e.g.: 2019_10_11_1) and a brief description of the actual change
- [ ] I have updated the revisionID in [bitrise_profile](roles/profiles/files/bitrise_profile) **BITRISE_OSX_STACK_REV_ID** with the one I just created in the CHANGELOG.md