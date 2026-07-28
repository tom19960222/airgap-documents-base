---
collection: ansible
version: "8"
title: "ansible.windows.win_wait_for module – Waits for a condition before continuing"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_wait_for_module.html
fetched_at: 2026-07-28T01:10:55+00:00
---
# ansible.windows.win_wait_for module – Waits for a condition before continuing

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_wait_for`.

- [Synopsis](win_wait_for_module.md#synopsis)
- [Parameters](win_wait_for_module.md#parameters)
- [See Also](win_wait_for_module.md#see-also)
- [Examples](win_wait_for_module.md#examples)
- [Return Values](win_wait_for_module.md#return-values)

## [Synopsis](win_wait_for_module.md#id1)

- You can wait for a set amount of time `timeout`, this is the default if nothing is specified.
- Waiting for a port to become available is useful for when services are not immediately available after their init scripts return which is true of certain Java application servers.
- You can wait for a file to exist or not exist on the filesystem.
- This module can also be used to wait for a regex match string to be present in a file.
- You can wait for active connections to be closed before continuing on a local port.

## [Parameters](win_wait_for_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **connect_timeout**  integer | The maximum number of seconds to wait for a connection to happen before closing and retrying.  **Default:** `5` |
| **delay**  integer | The number of seconds to wait before starting to poll. |
| **exclude_hosts**  list / elements=string | The list of hosts or IPs to ignore when looking for active TCP connections when `state=drained`. |
| **host**  string | A resolvable hostname or IP address to wait for.  If `state=drained` then it will only check for connections on the IP specified, you can use ‘0.0.0.0’ to use all host IPs.  **Default:** `"127.0.0.1"` |
| **path**  path | The path to a file on the filesystem to check.  If `state` is present or started then it will wait until the file exists.  If `state` is absent then it will wait until the file does not exist. |
| **port**  integer | The port number to poll on `host`. |
| **regex**  aliases: search_regex, regexp  string | Can be used to match a string in a file.  If `state` is present or started then it will wait until the regex matches.  If `state` is absent then it will wait until the regex does not match.  Defaults to a multiline regex. |
| **sleep**  integer | Number of seconds to sleep between checks.  **Default:** `1` |
| **state**  string | When checking a port, `started` will ensure the port is open, `stopped` will check that is it closed and `drained` will check for active connections.  When checking for a file or a search string `present` or `started` will ensure that the file or string is present, `absent` will check that the file or search string is absent or removed.  **Choices:**   - `"absent"` - `"drained"` - `"present"` - `"started"` ← (default) - `"stopped"` |
| **timeout**  integer | The maximum number of seconds to wait for.  **Default:** `300` |

## [See Also](win_wait_for_module.md#id3)

> **See also:**
>
> [ansible.builtin.wait_for](../builtin/wait_for_module.md#ansible-collections-ansible-builtin-wait-for-module)
> :   Waits for a condition before continuing.
>
> [community.windows.win_wait_for_process](../../community/windows/win_wait_for_process_module.md#ansible-collections-community-windows-win-wait-for-process-module)
> :   Waits for a process to exist or not exist before continuing.

## [Examples](win_wait_for_module.md#id4)

```yaml+jinja
- name: Wait 300 seconds for port 8000 to become open on the host, don't start checking for 10 seconds
  ansible.windows.win_wait_for:
    port: 8000
    delay: 10

- name: Wait 150 seconds for port 8000 of any IP to close active connections
  ansible.windows.win_wait_for:
    host: 0.0.0.0
    port: 8000
    state: drained
    timeout: 150

- name: Wait for port 8000 of any IP to close active connection, ignoring certain hosts
  ansible.windows.win_wait_for:
    host: 0.0.0.0
    port: 8000
    state: drained
    exclude_hosts: ['10.2.1.2', '10.2.1.3']

- name: Wait for file C:\temp\log.txt to exist before continuing
  ansible.windows.win_wait_for:
    path: C:\temp\log.txt

- name: Wait until process complete is in the file before continuing
  ansible.windows.win_wait_for:
    path: C:\temp\log.txt
    regex: process complete

- name: Wait until file is removed
  ansible.windows.win_wait_for:
    path: C:\temp\log.txt
    state: absent

- name: Wait until port 1234 is offline but try every 10 seconds
  ansible.windows.win_wait_for:
    port: 1234
    state: absent
    sleep: 10
```

## [Return Values](win_wait_for_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elapsed**  float | The elapsed seconds between the start of poll and the end of the module. This includes the delay if the option is set.  **Returned:** always  **Sample:** `2.1406487` |
| **wait_attempts**  integer | The number of attempts to poll the file or port before module finishes.  **Returned:** always  **Sample:** `1` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
