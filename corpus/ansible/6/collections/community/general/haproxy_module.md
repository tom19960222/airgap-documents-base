---
collection: ansible
version: "6"
title: "community.general.haproxy module – Enable, disable, and set weights for HAProxy backend servers using socket commands"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/haproxy_module.html
fetched_at: 2026-07-27T17:09:15+00:00
---
# community.general.haproxy module – Enable, disable, and set weights for HAProxy backend servers using socket commands

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.haproxy`.

- [Synopsis](haproxy_module.md#synopsis)
- [Parameters](haproxy_module.md#parameters)
- [Notes](haproxy_module.md#notes)
- [Examples](haproxy_module.md#examples)

## [Synopsis](haproxy_module.md#id1)

- Enable, disable, drain and set weights for HAProxy backend servers using socket commands.

## [Parameters](haproxy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **agent**  boolean  added in community.general 1.0.0 | Disable/enable agent checks (depending on *state* value).  Choices:   - `false` ← (default) - `true` |
| **backend**  string | Name of the HAProxy backend pool.  If this parameter is unset, it will be auto-detected. |
| **drain**  boolean | Wait until the server has no active connections or until the timeout determined by wait_interval and wait_retries is reached.  Continue only after the status changes to `MAINT`.  This overrides the shutdown_sessions option.  Choices:   - `false` ← (default) - `true` |
| **fail_on_not_found**  boolean | Fail whenever trying to enable/disable a backend host that does not exist.  Choices:   - `false` ← (default) - `true` |
| **health**  boolean  added in community.general 1.0.0 | Disable/enable health checks (depending on *state* value).  Choices:   - `false` ← (default) - `true` |
| **host**  string / required | Name of the backend host to change. |
| **shutdown_sessions**  boolean | When disabling a server, immediately terminate all the sessions attached to the specified server.  This can be used to terminate long-running sessions after a server is put into maintenance mode. Overridden by the drain option.  Choices:   - `false` ← (default) - `true` |
| **socket**  path | Path to the HAProxy socket file.  Default: `"/var/run/haproxy.sock"` |
| **state**  string / required | Desired state of the provided backend host.  Note that `drain` state was added in version 2.4.  It is supported only by HAProxy version 1.5 or later,  When used on versions < 1.5, it will be ignored.  Choices:   - `"disabled"` - `"drain"` - `"enabled"` |
| **wait**  boolean | Wait until the server reports a status of `UP` when *state=enabled*, status of `MAINT` when *state=disabled* or status of `DRAIN` when *state=drain*.  Choices:   - `false` ← (default) - `true` |
| **wait_interval**  integer | Number of seconds to wait between retries.  Default: `5` |
| **wait_retries**  integer | Number of times to check for status after changing the state.  Default: `25` |
| **weight**  string | The value passed in argument.  If the value ends with the `%` sign, then the new weight will be relative to the initially configured weight.  Relative weights are only permitted between 0 and 100% and absolute weights are permitted between 0 and 256. |

## [Notes](haproxy_module.md#id3)

> **Note:**
>
> - Enable, disable and drain commands are restricted and can only be issued on sockets configured for level ‘admin’. For example, you can add the line ‘stats socket /var/run/haproxy.sock level admin’ to the general section of haproxy.cfg. See <http://haproxy.1wt.eu/download/1.5/doc/configuration.txt>.
> - Depends on netcat (`nc`) being available; you need to install the appropriate package for your operating system before this module can be used.

## [Examples](haproxy_module.md#id4)

```yaml+jinja
- name: Disable server in 'www' backend pool
  community.general.haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    backend: www

- name: Disable server in 'www' backend pool, also stop health/agent checks
  community.general.haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    health: true
    agent: true

- name: Disable server without backend pool name (apply to all available backend pool)
  community.general.haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'

- name: Disable server, provide socket file
  community.general.haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    backend: www

- name: Disable server, provide socket file, wait until status reports in maintenance
  community.general.haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    backend: www
    wait: true

# Place server in drain mode, providing a socket file.  Then check the server's
# status every minute to see if it changes to maintenance mode, continuing if it
# does in an hour and failing otherwise.
- community.general.haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    backend: www
    wait: true
    drain: true
    wait_interval: 60
    wait_retries: 60

- name: Disable backend server in 'www' backend pool and drop open sessions to it
  community.general.haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    backend: www
    socket: /var/run/haproxy.sock
    shutdown_sessions: true

- name: Disable server without backend pool name (apply to all available backend pool) but fail when the backend host is not found
  community.general.haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    fail_on_not_found: true

- name: Enable server in 'www' backend pool
  community.general.haproxy:
    state: enabled
    host: '{{ inventory_hostname }}'
    backend: www

- name: Enable server in 'www' backend pool wait until healthy
  community.general.haproxy:
    state: enabled
    host: '{{ inventory_hostname }}'
    backend: www
    wait: true

- name: Enable server in 'www' backend pool wait until healthy. Retry 10 times with intervals of 5 seconds to retrieve the health
  community.general.haproxy:
    state: enabled
    host: '{{ inventory_hostname }}'
    backend: www
    wait: true
    wait_retries: 10
    wait_interval: 5

- name: Enable server in 'www' backend pool with change server(s) weight
  community.general.haproxy:
    state: enabled
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    weight: 10
    backend: www

- name: Set the server in 'www' backend pool to drain mode
  community.general.haproxy:
    state: drain
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    backend: www
```

### Authors

- Ravi Bhure (@ravibhure)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
