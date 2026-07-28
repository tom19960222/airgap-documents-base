---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_ucs_fetch module – Fetches a UCS file from remote nodes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_ucs_fetch_module.html
fetched_at: 2026-07-28T02:07:31+00:00
---
# f5networks.f5_modules.bigip_ucs_fetch module – Fetches a UCS file from remote nodes

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
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
| **async_timeout**  integer | Parameter used when creating new UCS file on a device.  The number of seconds to wait for the API async interface to complete its task.  The accepted value range is between `150` and `1800` seconds.  **Default:** `150` |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Creates a backup file including the timestamp information so you can get the original file back if you overwrote it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **create_on_missing**  boolean | Creates the UCS based on the value of `src`, if the file does not already exist on the remote system.  When set to `false`, with `fail_on_missing` set to `false` the module will return no change if the ucs file is missing on device.  **Choices:**   - `false` - `true` ← (default) |
| **dest**  path | A directory to save the UCS file into.  This option is mandatory when `only_create_file` is set to `false`. |
| **encryption_password**  string | Password to use to encrypt the UCS file if desired. |
| **fail_on_missing**  boolean | Make the module fail if the UCS file on the remote system is missing.  This option always takes precedence over `create_on_missing`, hence when set to `true`, the module will always fail if the UCS is missing, even if `create_on_missing` option is set to `true`.  When set to `false`, with `create_on_missing` set to `false` the module will return no change if the ucs file is missing on device.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | If `false`, the file is only transferred if the destination does not exist.  **Choices:**   - `false` - `true` ← (default) |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **only_create_file**  boolean  *added in f5networks.f5_modules 1.12.0* | If `true`, the file is created on the device and not downloaded. If the UCS archive exists on the device, no change is made and the file is not downloaded.  To recreate UCS files left on the device, remove them with the `bigip_ucs` module before running this module with `only_create_file` set to `true`.  **Choices:**   - `false` ← (default) - `true` |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **src**  string | The name of the UCS file to create on the remote server for downloading.  The file is retrieved or created in /var/local/ucs/.  This option is mandatory when `only_create_file` is set to `true`. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

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
    only_create_file: true
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
    only_create_file: true
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
| **backup_file**  string | Name of the backup file.  **Returned:** changed and if backup=yes  **Sample:** `"/path/to/file.txt.2015-02-12@22:09~"` |
| **checksum**  string | The SHA1 checksum of the downloaded file.  **Returned:** success or changed  **Sample:** `"7b46bbe4f8ebfee64761b5313855618f64c64109"` |
| **dest**  string | Location on the Ansible host the UCS was saved to.  **Returned:** success  **Sample:** `"/path/to/file.txt"` |
| **gid**  integer | Group ID of the UCS file, after execution.  **Returned:** success  **Sample:** `100` |
| **group**  string | Group of the UCS file, after execution.  **Returned:** success  **Sample:** `"httpd"` |
| **md5sum**  string | The MD5 checksum of the downloaded file.  **Returned:** changed or success  **Sample:** `"96cacab4c259c4598727d7cf2ceb3b45"` |
| **mode**  string | Permissions of the target UCS, after execution.  **Returned:** success  **Sample:** `"420"` |
| **owner**  string | Owner of the UCS file, after execution.  **Returned:** success  **Sample:** `"httpd"` |
| **size**  integer | Size of the target UCS, after execution.  **Returned:** success  **Sample:** `1220` |
| **src**  string | Name of the UCS file on the remote BIG-IP to download. If not specified, this is a randomly generated filename.  **Returned:** changed  **Sample:** `"cs_backup.ucs"` |
| **uid**  integer | Owner ID of the UCS file, after execution.  **Returned:** success  **Sample:** `100` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
