---
collection: ansible
version: "6"
title: "community.network.icx_copy module – Transfer files from or to remote Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/icx_copy_module.html
fetched_at: 2026-07-27T17:18:42+00:00
---
# community.network.icx_copy module – Transfer files from or to remote Ruckus ICX 7000 series switches

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.icx_copy`.

- [Synopsis](icx_copy_module.md#synopsis)
- [Parameters](icx_copy_module.md#parameters)
- [Notes](icx_copy_module.md#notes)
- [Examples](icx_copy_module.md#examples)
- [Return Values](icx_copy_module.md#return-values)

## [Synopsis](icx_copy_module.md#id1)

- This module transfers files from or to remote devices running ICX.

## [Parameters](icx_copy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **download**  string | Name of the resource to be downloaded. Mutually exclusive with upload.  Choices:   - `"running-config"` - `"startup-config"` - `"flash_primary"` - `"flash_secondary"` - `"bootrom"` - `"fips-primary-sig"` - `"fips-secondary-sig"` - `"fips-bootrom-sig"` |
| **protocol**  string / required | Data transfer protocol to be used  Choices:   - `"scp"` - `"https"` |
| **public_key**  string | public key type to be used to login to scp server  Choices:   - `"rsa"` - `"dsa"` |
| **remote_filename**  string / required | The name or path of the remote file/resource to be uploaded or downloaded. |
| **remote_pass**  string | remote password to be used for scp login. |
| **remote_port**  string | The port number of the remote host. Default values will be selected based on protocol type. Default scp:22, http:443 |
| **remote_server**  string / required | IP address of the remote server |
| **remote_user**  string | remote username to be used for scp login. |
| **upload**  string | Name of the resource to be uploaded. Mutually exclusive with download.  Choices:   - `"running-config"` - `"startup-config"` - `"flash_primary"` - `"flash_secondary"` |

## [Notes](icx_copy_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_copy_module.md#id4)

```yaml+jinja
- name: Upload running-config to the remote scp server
  community.network.icx_copy:
    upload: running-config
    protocol: scp
    remote_server: 172.16.10.49
    remote_filename: running.conf
    remote_user: user1
    remote_pass: pass123

- name: Download running-config from the remote scp server
  community.network.icx_copy:
    download: running-config
    protocol: scp
    remote_server: 172.16.10.49
    remote_filename: running.conf
    remote_user: user1
    remote_pass: pass123

- name: Download running-config from the remote scp server using rsa public key
  community.network.icx_copy:
    download: running-config
    protocol: scp
    remote_server: 172.16.10.49
    remote_filename: running.conf
    remote_user: user1
    remote_pass: pass123
    public_key: rsa

- name: Upload startup-config to the remote https server
  community.network.icx_copy:
    upload: startup-config
    protocol: https
    remote_server: 172.16.10.49
    remote_filename: config/running.conf
    remote_user: user1
    remote_pass: pass123

- name: Upload startup-config to the remote https server
  community.network.icx_copy:
    upload: startup-config
    protocol: https
    remote_server: 172.16.10.49
    remote_filename: config/running.conf
    remote_user: user1
    remote_pass: pass123

- name: Download OS image into the flash from remote scp ipv6 server
  community.network.icx_copy:
    download: startup-config
    protocol: scp
    remote_server: ipv6 FE80:CD00:0000:0CDE:1257:0000:211E:729C
    remote_filename: img.bin
    remote_user: user1
    remote_pass: pass123

- name: Download OS image into the secondary flash from remote scp ipv6 server
  community.network.icx_copy:
    Download: flash_secondary
    protocol: scp
    remote_server: ipv6 FE80:CD00:0000:0CDE:1257:0000:211E:729C
    remote_filename: img.bin
    remote_user: user1
    remote_pass: pass123

- name: Download OS image into the secondary flash from remote scp ipv6 server on port 5000
  community.network.icx_copy:
    Download: flash_secondary
    protocol: scp
    remote_server: ipv6 FE80:CD00:0000:0CDE:1257:0000:211E:729C
    remote_port: 5000
    remote_filename: img.bin
    remote_user: user1
    remote_pass: pass123

- name: Download OS image into the primary flash from remote https ipv6 server
  community.network.icx_copy:
    Download: flash_primary
    protocol: https
    remote_server: ipv6 FE80:CD00:0000:0CDE:1257:0000:211E:729C
    remote_filename: images/img.bin
    remote_user: user1
    remote_pass: pass123

- name: Download OS image into the primary flash from remote https ipv6 server on port 8080
  community.network.icx_copy:
    Download: flash_primary
    protocol: https
    remote_server: ipv6 FE80:CD00:0000:0CDE:1257:0000:211E:729C
    remote_port: 8080
    remote_filename: images/img.bin
    remote_user: user1
    remote_pass: pass123
```

## [Return Values](icx_copy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | true when downloaded any configuration or flash. false otherwise.  Returned: always |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
