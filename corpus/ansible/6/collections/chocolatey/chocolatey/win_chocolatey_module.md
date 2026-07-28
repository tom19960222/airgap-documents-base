---
collection: ansible
version: "6"
title: "chocolatey.chocolatey.win_chocolatey module – Manage packages using chocolatey"
source_url: https://docs.ansible.com/projects/ansible/6/collections/chocolatey/chocolatey/win_chocolatey_module.html
fetched_at: 2026-07-27T16:48:59+00:00
---
# chocolatey.chocolatey.win_chocolatey module – Manage packages using chocolatey

> **Note:**
>
> This module is part of the [chocolatey.chocolatey collection](https://galaxy.ansible.com/chocolatey/chocolatey) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install chocolatey.chocolatey`.
> You need further requirements to be able to use this module,
> see [Requirements](win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module-requirements) for details.
>
> To use it in a playbook, specify: `chocolatey.chocolatey.win_chocolatey`.

New in chocolatey.chocolatey 0.1.9

- [Synopsis](win_chocolatey_module.md#synopsis)
- [Requirements](win_chocolatey_module.md#requirements)
- [Parameters](win_chocolatey_module.md#parameters)
- [Notes](win_chocolatey_module.md#notes)
- [See Also](win_chocolatey_module.md#see-also)
- [Examples](win_chocolatey_module.md#examples)
- [Return Values](win_chocolatey_module.md#return-values)

## [Synopsis](win_chocolatey_module.md#id1)

- Manage packages using Chocolatey.
- If Chocolatey is missing from the system, the module will install it.

## [Requirements](win_chocolatey_module.md#id2)

The below requirements are needed on the host that executes this module.

- chocolatey >= 0.10.5 (will be upgraded if older)

## [Parameters](win_chocolatey_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_empty_checksums**  boolean  added in chocolatey.chocolatey 0.2.2 | Allow empty checksums to be used for downloaded resource from non-secure locations.  Use [chocolatey.chocolatey.win_chocolatey_feature](win_chocolatey_feature_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-feature-module) with the name `allowEmptyChecksums` to control this option globally.  Choices:   - `false` ← (default) - `true` |
| **allow_multiple**  boolean  added in chocolatey.chocolatey 0.2.8 | Allow the installation of multiple packages when *version* is specified.  Having multiple packages at different versions can cause issues if the package doesn’t support this. Use at your own risk.  The value of this parameter is ignored if *state* is `absent`. Instead, this parameter is automatically configured to remove all versions if *version* is not specified, and the specific version only if *version* is specified.  Choices:   - `false` ← (default) - `true` |
| **allow_prerelease**  boolean  added in chocolatey.chocolatey 0.2.6 | Allow the installation of pre-release packages.  If *state* is `latest`, the latest pre-release package will be installed.  Choices:   - `false` ← (default) - `true` |
| **architecture**  string  added in chocolatey.chocolatey 0.2.7 | Force Chocolatey to install the package of a specific process architecture.  When setting `x86`, will ensure Chocolatey installs the x86 package even when on an x64 bit OS.  Choices:   - `"default"` ← (default) - `"x86"` |
| **bootstrap_script**  aliases: install_ps1, bootstrap_ps1  string  added in chocolatey.chocolatey 1.3.0 | Specify the bootstrap script URL that can be used to install Chocolatey if it is not already present on the system.  Use this parameter when *name* is `chocolatey` to ensure that a custom bootstrap script is used.  If neither this parameter nor *source* is set, the bootstrap script url will be `https://community.chocolatey.org/install.ps1`  If this parameter is not set, and *source* is set to a url, the bootstrap script url will be determined from that url instead.  This parameter only defines which bootstrap script is used to download and install Chocolatey. To define the URL to a specific Chocolatey nupkg to install, note that many bootstrap scripts respect the value of the `chocolateyDownloadUrl` environment variable, which can be set for the task as well. |
| **choco_args**  aliases: licensed_args  list / elements=string  added in chocolatey.chocolatey 1.2.0 | Additional parameters to pass to choco.exe  These may be any additional parameters to pass through directly to Chocolatey, in addition to the arguments already specified via other parameters.  This may be used to pass licensed options to Chocolatey, for example `--package-parameters-sensitive` or `--install-directory`.  Passing licensed options may result in them being ignored or causing errors if the targeted node is unlicensed or missing the chocolatey.extension package. |
| **force**  boolean | Forces the install of a package, even if it already is installed.  Using *force* will cause Ansible to always report that a change was made.  Choices:   - `false` ← (default) - `true` |
| **ignore_checksums**  boolean  added in chocolatey.chocolatey 0.2.2 | Ignore the checksums provided by the package.  Use [chocolatey.chocolatey.win_chocolatey_feature](win_chocolatey_feature_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-feature-module) with the name `checksumFiles` to control this option globally.  Choices:   - `false` ← (default) - `true` |
| **ignore_dependencies**  boolean  added in chocolatey.chocolatey 0.2.1 | Ignore dependencies, only install/upgrade the package itself.  Choices:   - `false` ← (default) - `true` |
| **install_args**  string  added in chocolatey.chocolatey 0.2.1 | Arguments to pass to the native installer.  These are arguments that are passed directly to the installer the Chocolatey package runs, this is generally an advanced option. |
| **name**  list / elements=string / required | Name of the package(s) to be installed.  Set to `all` to run the action on all the installed packages. |
| **override_args**  boolean  added in chocolatey.chocolatey 0.2.10 | Override arguments of native installer with arguments provided by user.  Should install arguments be used exclusively without appending to current package passed arguments.  Choices:   - `false` ← (default) - `true` |
| **package_params**  aliases: params  string  added in chocolatey.chocolatey 0.2.1 | Parameters to pass to the package.  These are parameters specific to the Chocolatey package and are generally documented by the package itself.  Before Ansible 2.7, this option was just *params*. |
| **pinned**  boolean  added in chocolatey.chocolatey 0.2.8 | Whether to pin the Chocolatey package or not.  If omitted then no checks on package pins are done.  Will pin/unpin the specific version if *version* is set.  Will pin the latest version of a package if `yes`, *version* is not set and and no pin already exists.  Will unpin all versions of a package if `no` and *version* is not set.  This is ignored when `state=absent`.  Choices:   - `false` - `true` |
| **proxy_password**  string  added in chocolatey.chocolatey 0.2.4 | Proxy password used to install Chocolatey and the package.  This value is exposed as a command argument and any privileged account can see this value when the module is running Chocolatey, define the password on the global config level with [chocolatey.chocolatey.win_chocolatey_config](win_chocolatey_config_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-config-module) with name `proxyPassword` to avoid this. |
| **proxy_url**  string  added in chocolatey.chocolatey 0.2.4 | Proxy URL used to install chocolatey and the package.  Use [chocolatey.chocolatey.win_chocolatey_config](win_chocolatey_config_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-config-module) with the name `proxy` to control this option globally. |
| **proxy_username**  string  added in chocolatey.chocolatey 0.2.4 | Proxy username used to install Chocolatey and the package.  Before Ansible 2.7, users with double quote characters `"` would need to be escaped with `\` beforehand. This is no longer necessary.  Use [chocolatey.chocolatey.win_chocolatey_config](win_chocolatey_config_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-config-module) with the name `proxyUser` to control this option globally. |
| **remove_dependencies**  boolean  added in chocolatey.chocolatey 1.1.0 | Remove a package’s dependencies on uninstall.  Choices:   - `false` ← (default) - `true` |
| **skip_scripts**  boolean  added in chocolatey.chocolatey 0.2.4 | Do not run *chocolateyInstall.ps1* or *chocolateyUninstall.ps1* scripts when installing a package.  Choices:   - `false` ← (default) - `true` |
| **source**  string | Specify the source to retrieve the package from.  Use [chocolatey.chocolatey.win_chocolatey_source](win_chocolatey_source_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-source-module) to manage global sources.  This value can either be the URL to a Chocolatey feed, a path to a folder containing `.nupkg` packages or the name of a source defined by [chocolatey.chocolatey.win_chocolatey_source](win_chocolatey_source_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-source-module).  When Chocolatey is not yet installed, prefer using *bootstrap_script* instead to determine where to pull the bootstrap script from.  This value may also be used when Chocolatey is not installed as the location of the install.ps1 script if *bootstrap_script* is not set, and only supports URLs for this case. In this case, if the URL ends in “.ps1”, it is used as-is. Otherwise, if the URL appears to contain a “/repository/” fragment, the module will attempt to append “/install.ps1” to find an install script. If neither of these checks pass, the module will strip off the URL path and try to find an “/install.ps1” from the root of the server. |
| **source_password**  string  added in chocolatey.chocolatey 0.2.7 | The password for *source_username*.  This value is exposed as a command argument and any privileged account can see this value when the module is running Chocolatey, define the credentials with a source with [chocolatey.chocolatey.win_chocolatey_source](win_chocolatey_source_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-source-module) to avoid this. |
| **source_username**  string  added in chocolatey.chocolatey 0.2.7 | A username to use with *source* when accessing a feed that requires authentication.  It is recommended you define the credentials on a source with [chocolatey.chocolatey.win_chocolatey_source](win_chocolatey_source_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-source-module) instead of passing it per task. |
| **state**  string | State of the package on the system.  When `absent`, will ensure the package is not installed.  When `present`, will ensure the package is installed.  When `downgrade`, will allow Chocolatey to downgrade a package if *version* is older than the installed version.  When `latest` or `upgrade`, will ensure the package is installed to the latest available version.  When `reinstalled`, will uninstall and reinstall the package.  Choices:   - `"absent"` - `"downgrade"` - `"upgrade"` - `"latest"` - `"present"` ← (default) - `"reinstalled"` |
| **timeout**  aliases: execution_timeout  integer  added in chocolatey.chocolatey 0.2.3 | The time to allow chocolatey to finish before timing out.  Default: `2700` |
| **validate_certs**  boolean  added in chocolatey.chocolatey 0.2.7 | Used when downloading the Chocolatey install script if Chocolatey is not already installed, this does not affect the Chocolatey package install process.  When `no`, no SSL certificates will be validated.  This should only be used on personally controlled sites using self-signed certificate.  Choices:   - `false` - `true` ← (default) |
| **version**  string | Specific version of the package to be installed.  When *state* is set to `absent`, will uninstall the specific version otherwise all versions of that package will be removed.  When *state* is set to `present` and the package is already installed at a version that does not match, this task fails.  If a different version of package is already installed, *state* must be `latest`, `upgrade`, or `downgrade`, or *force* must be set to `yes` to install the desired version.  Provide as a string (e.g. `'6.1'`), otherwise it is considered to be a floating-point number and depending on the locale could become `6,1`, which will cause a failure.  If *name* is set to `chocolatey` and Chocolatey is not installed on the host, this will be the version of Chocolatey that is installed. You can also set the `chocolateyVersion` environment var. |

## [Notes](win_chocolatey_module.md#id4)

> **Note:**
>
> - This module will install or upgrade Chocolatey when needed.
> - When using verbosity 2 or less (`-vv`) the `stdout` output will be restricted. When using verbosity 4 (`-vvvv`) the `stdout` output will be more verbose. When using verbosity 5 (`-vvvvv`) the `stdout` output will include debug output.
> - Some packages, like hotfixes or updates need an interactive user logon in order to install. You can use `become` to achieve this, see :ref:`become_windows`. Even if you are connecting as local Administrator, using `become` to become Administrator will give you an interactive user logon, see examples below.
> - If `become` is unavailable, use [community.windows.win_hotfix](../../community/windows/win_hotfix_module.md#ansible-collections-community-windows-win-hotfix-module) to install hotfixes instead of [chocolatey.chocolatey.win_chocolatey](win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module) as [community.windows.win_hotfix](../../community/windows/win_hotfix_module.md#ansible-collections-community-windows-win-hotfix-module) avoids using `wusa.exe` which cannot be run without `become`.

## [See Also](win_chocolatey_module.md#id5)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey_config](win_chocolatey_config_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-config-module)
> :   Manages Chocolatey config settings.
>
> [chocolatey.chocolatey.win_chocolatey_facts](win_chocolatey_facts_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-facts-module)
> :   Create a facts collection for Chocolatey.
>
> [chocolatey.chocolatey.win_chocolatey_feature](win_chocolatey_feature_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-feature-module)
> :   Manages Chocolatey features.
>
> [chocolatey.chocolatey.win_chocolatey_source](win_chocolatey_source_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-source-module)
> :   Manages Chocolatey sources.
>
> community.windows.win_feature
> :   The official documentation on the **community.windows.win_feature** module.
>
> [community.windows.win_hotfix](../../community/windows/win_hotfix_module.md#ansible-collections-community-windows-win-hotfix-module)
> :   Use when `become` is unavailable, to avoid using `wusa.exe`.
>
> community.windows.win_package
> :   The official documentation on the **community.windows.win_package** module.
>
> community.windows.win_updates
> :   The official documentation on the **community.windows.win_updates** module.
>
> [Chocolatey website](http://chocolatey.org/)
> :   More information about the Chocolatey tool.
>
> [Chocolatey packages](http://chocolatey.org/packages)
> :   An overview of the available Chocolatey packages.
>
> [Become and Windows](../../../user_guide/become.md#become-windows)
> :   Some packages, like hotfixes or updates need an interactive user logon in order to install. You can use `become` to achieve this.

## [Examples](win_chocolatey_module.md#id6)

```yaml+jinja
- name: Install git
  win_chocolatey:
    name: git
    state: present

- name: Upgrade installed packages
  win_chocolatey:
    name: all
    state: latest

- name: Install notepadplusplus version 6.6
  win_chocolatey:
    name: notepadplusplus
    version: '6.6'

- name: Install notepadplusplus 32 bit version
  win_chocolatey:
    name: notepadplusplus
    architecture: x86

- name: Install git from specified repository
  win_chocolatey:
    name: git
    source: https://someserver/api/v2/

- name: Install git from a pre configured source (win_chocolatey_source)
  win_chocolatey:
    name: git
    source: internal_repo

- name: Ensure Chocolatey itself is installed, using community repo for the bootstrap
  win_chocolatey:
    name: chocolatey

- name: Ensure Chocolatey itself is installed, bootstrapping with a specific nupkg url
  win_chocolatey:
    name: chocolatey
  environment:
    - chocolateyDownloadUrl: "https://internal-web-server/files/chocolatey.1.1.0.nupkg"

- name: Ensure Chocolatey itself is installed and use internal repo as source for bootstrap script
  win_chocolatey:
    name: chocolatey
    source: http://someserver/chocolatey

- name: Ensure Chocolatey itself is installed, using a specific bootstrap script
  win_chocolatey:
    name: chocolatey
    bootstrap_script: https://internal-web-server/files/custom-chocolatey-install.ps1

- name: Ensure Chocolatey itself is installed, using a specific bootstrap script and target nupkg
  win_chocolatey:
    name: chocolatey
    bootstrap_script: https://internal-web-server/files/custom-chocolatey-install.ps1
  environment:
    - chocolateyDownloadUrl: "https://internal-web-server/files/chocolatey.1.1.0.nupkg"

- name: Uninstall git
  win_chocolatey:
    name: git
    state: absent

- name: Install multiple packages
  win_chocolatey:
    name:
    - procexp
    - putty
    - windirstat
    state: present

- name: Install multiple packages sequentially
  win_chocolatey:
    name: '{{ item }}'
    state: present
  loop:
  - procexp
  - putty
  - windirstat

- name: Uninstall multiple packages
  win_chocolatey:
    name:
    - procexp
    - putty
    - windirstat
    state: absent

- name: Uninstall a package and dependencies
  win_chocolatey:
    name: audacity-lame
    remove_dependencies: yes
    state: absent

- name: Install curl using proxy
  win_chocolatey:
    name: curl
    proxy_url: http://proxy-server:8080/
    proxy_username: joe
    proxy_password: p@ssw0rd

- name: Install a package that requires 'become'
  win_chocolatey:
    name: officepro2013
  become: yes
  become_user: Administrator
  become_method: runas

- name: install and pin Notepad++ at 7.6.3
  win_chocolatey:
    name: notepadplusplus
    version: 7.6.3
    pinned: yes
    state: present

- name: remove all pins for Notepad++ on all versions
  win_chocolatey:
    name: notepadplusplus
    pinned: no
    state: present

- name: install a package with options that require licensed edition
  win_chocolatey:
    name: foo
    state: present
    choco_args:
    - --skip-download-cache
    - --package-parameters-sensitive
    - '/Password=SecretPassword'
```

## [Return Values](win_chocolatey_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | The full command used in the chocolatey task.  Returned: changed  Sample: `"choco.exe install -r --no-progress -y sysinternals --timeout 2700 --failonunfound"` |
| **rc**  integer | The return code from the chocolatey task.  Returned: always  Sample: `0` |
| **stdout**  string | The stdout from the chocolatey task. The verbosity level of the messages are affected by Ansible verbosity setting, see notes for more details.  Returned: changed  Sample: `"Chocolatey upgraded 1/1 packages."` |

### Authors

- Trond Hindenes (@trondhindenes)
- Peter Mounce (@petemounce)
- Pepe Barbe (@elventear)
- Adam Keech (@smadam813)
- Pierre Templier (@ptemplier)
- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/chocolatey/chocolatey-ansible/issues)
[Repository (Sources)](https://github.com/chocolatey/chocolatey-ansible)
