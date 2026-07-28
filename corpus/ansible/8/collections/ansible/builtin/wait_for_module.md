---
collection: ansible
version: "8"
title: "ansible.builtin.wait_for module – Waits for a condition before continuing"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/wait_for_module.html
fetched_at: 2026-07-28T01:07:49+00:00
---
# ansible.builtin.wait_for module – Waits for a condition before continuing

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `wait_for` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.wait_for` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](wait_for_module.md#synopsis)
- [Parameters](wait_for_module.md#parameters)
- [Attributes](wait_for_module.md#attributes)
- [Notes](wait_for_module.md#notes)
- [See Also](wait_for_module.md#see-also)
- [Examples](wait_for_module.md#examples)
- [Return Values](wait_for_module.md#return-values)

## [Synopsis](wait_for_module.md#id1)

- You can wait for a set amount of time `timeout`, this is the default if nothing is specified or just `timeout` is specified. This does not produce an error.
- Waiting for a port to become available is useful for when services are not immediately available after their init scripts return which is true of certain Java application servers.
- It is also useful when starting guests with the [community.libvirt.virt](../../community/libvirt/virt_module.md#ansible-collections-community-libvirt-virt-module) module and needing to pause until they are ready.
- This module can also be used to wait for a regex match a string to be present in a file.
- In Ansible 1.6 and later, this module can also be used to wait for a file to be available or absent on the filesystem.
- In Ansible 1.8 and later, this module can also be used to wait for active connections to be closed before continuing, useful if a node is being rotated out of a load balancer pool.
- For Windows targets, use the [ansible.windows.win_wait_for](../windows/win_wait_for_module.md#ansible-collections-ansible-windows-win-wait-for-module) module instead.

## [Parameters](wait_for_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **active_connection_states**  list / elements=string | The list of TCP connection states which are counted as active connections.  **Default:** `["ESTABLISHED", "FIN_WAIT1", "FIN_WAIT2", "SYN_RECV", "SYN_SENT", "TIME_WAIT"]` |
| **connect_timeout**  integer | Maximum number of seconds to wait for a connection to happen before closing and retrying.  **Default:** `5` |
| **delay**  integer | Number of seconds to wait before starting to poll.  **Default:** `0` |
| **exclude_hosts**  list / elements=string | List of hosts or IPs to ignore when looking for active TCP connections for `drained` state. |
| **host**  string | A resolvable hostname or IP address to wait for.  **Default:** `"127.0.0.1"` |
| **msg**  string | This overrides the normal error message from a failure to meet the required conditions. |
| **path**  path | Path to a file on the filesystem that must exist before continuing.  `path` and `port` are mutually exclusive parameters. |
| **port**  integer | Port number to poll.  `path` and `port` are mutually exclusive parameters. |
| **search_regex**  string | Can be used to match a string in either a file or a socket connection.  Defaults to a multiline regex. |
| **sleep**  integer | Number of seconds to sleep between checks.  Before Ansible 2.3 this was hardcoded to 1 second.  **Default:** `1` |
| **state**  string | Either `present`, `started`, or `stopped`, `absent`, or `drained`.  When checking a port `started` will ensure the port is open, `stopped` will check that it is closed, `drained` will check for active connections.  When checking for a file or a search string `present` or `started` will ensure that the file or string is present before continuing, `absent` will check that file is absent or removed.  **Choices:**   - `"absent"` - `"drained"` - `"present"` - `"started"` ← (default) - `"stopped"` |
| **timeout**  integer | Maximum number of seconds to wait for, when used with another condition it will force an error.  When used without other conditions it is equivalent of just sleeping.  **Default:** `300` |

## [Attributes](wait_for_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Notes](wait_for_module.md#id4)

> **Note:**
>
> - The ability to use search_regex with a port connection was added in Ansible 1.7.
> - Prior to Ansible 2.4, testing for the absence of a directory or UNIX socket did not work correctly.
> - Prior to Ansible 2.4, testing for the presence of a file did not work correctly if the remote user did not have read access to that file.
> - Under some circumstances when using mandatory access control, a path may always be treated as being absent even if it exists, but can’t be modified or created by the remote user either.
> - When waiting for a path, symbolic links will be followed. Many other modules that manipulate files do not follow symbolic links, so operations on the path using other modules may not work exactly as expected.

## [See Also](wait_for_module.md#id5)

> **See also:**
>
> [ansible.builtin.wait_for_connection](wait_for_connection_module.md#ansible-collections-ansible-builtin-wait-for-connection-module)
> :   Waits until remote system is reachable/usable.
>
> [ansible.windows.win_wait_for](../windows/win_wait_for_module.md#ansible-collections-ansible-windows-win-wait-for-module)
> :   Waits for a condition before continuing.
>
> [community.windows.win_wait_for_process](../../community/windows/win_wait_for_process_module.md#ansible-collections-community-windows-win-wait-for-process-module)
> :   Waits for a process to exist or not exist before continuing.

## [Examples](wait_for_module.md#id6)

```yaml+jinja
- name: Sleep for 300 seconds and continue with play
  ansible.builtin.wait_for:
    timeout: 300
  delegate_to: localhost

- name: Wait for port 8000 to become open on the host, don't start checking for 10 seconds
  ansible.builtin.wait_for:
    port: 8000
    delay: 10

- name: Waits for port 8000 of any IP to close active connections, don't start checking for 10 seconds
  ansible.builtin.wait_for:
    host: 0.0.0.0
    port: 8000
    delay: 10
    state: drained

- name: Wait for port 8000 of any IP to close active connections, ignoring connections for specified hosts
  ansible.builtin.wait_for:
    host: 0.0.0.0
    port: 8000
    state: drained
    exclude_hosts: 10.2.1.2,10.2.1.3

- name: Wait until the file /tmp/foo is present before continuing
  ansible.builtin.wait_for:
    path: /tmp/foo

- name: Wait until the string "completed" is in the file /tmp/foo before continuing
  ansible.builtin.wait_for:
    path: /tmp/foo
    search_regex: completed

- name: Wait until regex pattern matches in the file /tmp/foo and print the matched group
  ansible.builtin.wait_for:
    path: /tmp/foo
    search_regex: completed (?P<task>\w+)
  register: waitfor
- ansible.builtin.debug:
    msg: Completed {{ waitfor['match_groupdict']['task'] }}

- name: Wait until the lock file is removed
  ansible.builtin.wait_for:
    path: /var/lock/file.lock
    state: absent

- name: Wait until the process is finished and pid was destroyed
  ansible.builtin.wait_for:
    path: /proc/3466/status
    state: absent

- name: Output customized message when failed
  ansible.builtin.wait_for:
    path: /tmp/foo
    state: present
    msg: Timeout to find file /tmp/foo

# Do not assume the inventory_hostname is resolvable and delay 10 seconds at start
- name: Wait 300 seconds for port 22 to become open and contain "OpenSSH"
  ansible.builtin.wait_for:
    port: 22
    host: '{{ (ansible_ssh_host|default(ansible_host))|default(inventory_hostname) }}'
    search_regex: OpenSSH
    delay: 10
  connection: local

# Same as above but you normally have ansible_connection set in inventory, which overrides 'connection'
- name: Wait 300 seconds for port 22 to become open and contain "OpenSSH"
  ansible.builtin.wait_for:
    port: 22
    host: '{{ (ansible_ssh_host|default(ansible_host))|default(inventory_hostname) }}'
    search_regex: OpenSSH
    delay: 10
  vars:
    ansible_connection: local
```

## [Return Values](wait_for_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elapsed**  integer | The number of seconds that elapsed while waiting  **Returned:** always  **Sample:** `23` |
| **match_groupdict**  dictionary | Dictionary containing all the named subgroups of the match, keyed by the subgroup name, as returned by <https://docs.python.org/3/library/re.html#re.MatchObject.groupdict>  **Returned:** always  **Sample:** `{"group": "match"}` |
| **match_groups**  list / elements=string | Tuple containing all the subgroups of the match as returned by <https://docs.python.org/3/library/re.html#re.MatchObject.groups>  **Returned:** always  **Sample:** `["match 1", "match 2"]` |

### Authors

- Jeroen Hoekx (@jhoekx)
- John Jarvis (@jarv)
- Andrii Radyk (@AnderEnder)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
