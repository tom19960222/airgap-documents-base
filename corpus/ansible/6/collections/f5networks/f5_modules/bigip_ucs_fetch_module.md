---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_ucs_fetch module – Fetches a UCS file from remote nodes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_ucs_fetch_module.html
fetched_at: 2026-07-27T17:28:00+00:00
---
# f5networks.f5_modules.bigip_ucs_fetch module – Fetches a UCS file from remote nodes

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_ucs_fetch`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_ucs_fetch_module.md#synopsis)
- [Parameters](bigip_ucs_fetch_module.md#parameters)
- [Notes](bigip_ucs_fetch_module.md#notes)
- [Examples](bigip_ucs_fetch_module.md#examples)
- [Return Values](bigip_ucs_fetch_module.md#return-values)

## [Synopsis](bigip_ucs_fetch_module.md#id1)

- This module is used for fetching UCS files from remote machines and storing them locally in a file tree, organized by hostname. This module was written to create and transfer UCS files that might not be present, it does not require UCS file to be pre-created. So a missing remote UCS is not an error unless `fail_on_missing` is set to ‘yes’.

## [Parameters](bigip_ucs_fetch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **async_timeout**  integer | Parameter used when creating new UCS file on a device.  The amount of time to wait for the API async interface to complete its task, in seconds.  The accepted value range is between `150` and `1800` seconds.  Default: `150` |
| **backup**  boolean | Creates a backup file including the timestamp information so you can get the original file back if you overwrote it incorrectly.  Choices:   - `false` ← (default) - `true` |
| **create_on_missing**  boolean | Creates the UCS based on the value of `src`, if the file does not already exist on the remote system.  Choices:   - `false` - `true` ← (default) |
| **dest**  path | A directory to save the UCS file into.  This option is mandatory when `only_create_file` is set to `no`. |
| **encryption_password**  string | Password to use to encrypt the UCS file if desired. |
| **fail_on_missing**  boolean | Make the module fail if the UCS file on the remote system is missing.  Choices:   - `false` ← (default) - `true` |
| **force**  boolean | If `no`, the file is only transferred if the destination does not exist.  Choices:   - `false` - `true` ← (default) |
| **only_create_file**  boolean  added in f5networks.f5_modules 1.12.0 | If `yes`, the file is created on device and not downloaded. If the UCS archive exists on device, no change is made and file is not be downloaded.  To recreate UCS files left on the device, remove them with `bigip_ucs` module before running this module with `only_create_file` set to `yes`.  Choices:   - `false` ← (default) - `true` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **src**  string | The name of the UCS file to create on the remote server for downloading.  The file is retrieved or created in /var/local/ucs/.  This option is mandatory when `only_create_file` is set to `yes`. |

## [Notes](bigip_ucs_fetch_module.md#id3)

> **Note:**
>
> - BIG-IP provides no way to get a checksum of the UCS files on the system via any interface with the possible exception of logging in directly to the box (which would not support appliance mode). Therefore, the best this module can do is check for the existence of the file on disk; no check-summing.
> - If you are using this module with either Ansible Tower or Ansible AWX, you should be aware of how these Ansible products execute jobs in restricted environments. More information can be found here <https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/module-usage-with-tower.html>
> - Some longer running tasks might cause the REST interface on BIG-IP to time out, to avoid this adjust the timers as per this KB article <https://support.f5.com/csp/article/K94602685>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_ucs_fetch_module.md#id4)

```yaml+jinja
- name: Download a new UCS
  bigip_ucs_fetch:
    src: cs_backup.ucs
    dest: /tmp/cs_backup.ucs
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Only create new UCS, no download
  bigip_ucs_fetch:
    src: cs_backup.ucs
    only_create_file: yes
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Recreate UCS file left on device - remove file first
  bigip_ucs:
    ucs: cs_backup.ucs
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Recreate UCS file left on device - create new file
  bigip_ucs_fetch:
    src: cs_backup.ucs
    only_create_file: yes
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_ucs_fetch_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of the backup file.  Returned: changed and if backup=yes  Sample: `"/path/to/file.txt.2015-02-12@22:09~"` |
| **checksum**  string | The SHA1 checksum of the downloaded file.  Returned: success or changed  Sample: `"7b46bbe4f8ebfee64761b5313855618f64c64109"` |
| **dest**  string | Location on the ansible host the UCS was saved to.  Returned: success  Sample: `"/path/to/file.txt"` |
| **gid**  integer | Group ID of the UCS file, after execution.  Returned: success  Sample: `100` |
| **group**  string | Group of the UCS file, after execution.  Returned: success  Sample: `"httpd"` |
| **md5sum**  string | The MD5 checksum of the downloaded file.  Returned: changed or success  Sample: `"96cacab4c259c4598727d7cf2ceb3b45"` |
| **mode**  string | Permissions of the target UCS, after execution.  Returned: success  Sample: `"420"` |
| **owner**  string | Owner of the UCS file, after execution.  Returned: success  Sample: `"httpd"` |
| **size**  integer | Size of the target UCS, after execution.  Returned: success  Sample: `1220` |
| **src**  string | Name of the UCS file on the remote BIG-IP to download. If not specified, this is a randomly generated filename.  Returned: changed  Sample: `"cs_backup.ucs"` |
| **uid**  integer | Owner ID of the UCS file, after execution.  Returned: success  Sample: `100` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
