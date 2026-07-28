---
collection: ansible
version: "8"
title: "arista.eos.eos_eapi module – Manage and configure Arista EOS eAPI."
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_eapi_module.html
fetched_at: 2026-07-28T01:05:29+00:00
---
# arista.eos.eos_eapi module – Manage and configure Arista EOS eAPI.

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
> You need further requirements to be able to use this module,
> see [Requirements](eos_eapi_module.md#ansible-collections-arista-eos-eos-eapi-module-requirements) for details.
>
> To use it in a playbook, specify: `arista.eos.eos_eapi`.

New in arista.eos 1.0.0

- [Synopsis](eos_eapi_module.md#synopsis)
- [Requirements](eos_eapi_module.md#requirements)
- [Parameters](eos_eapi_module.md#parameters)
- [Examples](eos_eapi_module.md#examples)
- [Return Values](eos_eapi_module.md#return-values)

## [Synopsis](eos_eapi_module.md#id1)

- Use to enable or disable eAPI access, and set the port and state of http, https, local_http and unix-socket servers.
- When enabling eAPI access the default is to enable HTTP on port 80, enable HTTPS on port 443, disable local HTTP, and disable Unix socket server. Use the options listed below to override the default configuration.
- Requires EOS v4.12 or greater.

Aliases: eapi

## [Requirements](eos_eapi_module.md#id2)

The below requirements are needed on the host that executes this module.

- EOS v4.12 or greater

## [Parameters](eos_eapi_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **http**  aliases: enable_http  boolean | The `http` argument controls the operating state of the HTTP transport protocol when eAPI is present in the running-config. When the value is set to True, the HTTP protocol is enabled and when the value is set to False, the HTTP protocol is disabled. By default, when eAPI is first configured, the HTTP protocol is disabled.  **Choices:**   - `false` - `true` |
| **http_port**  integer | Configures the HTTP port that will listen for connections when the HTTP transport protocol is enabled. This argument accepts integer values in the valid range of 1 to 65535. |
| **https**  aliases: enable_https  boolean | The `https` argument controls the operating state of the HTTPS transport protocol when eAPI is present in the running-config. When the value is set to True, the HTTPS protocol is enabled and when the value is set to False, the HTTPS protocol is disabled. By default, when eAPI is first configured, the HTTPS protocol is enabled.  **Choices:**   - `false` - `true` |
| **https_port**  integer | Configures the HTTP port that will listen for connections when the HTTP transport protocol is enabled. This argument accepts integer values in the valid range of 1 to 65535. |
| **local_http**  aliases: enable_local_http  boolean | The `local_http` argument controls the operating state of the local HTTP transport protocol when eAPI is present in the running-config. When the value is set to True, the HTTP protocol is enabled and restricted to connections from localhost only. When the value is set to False, the HTTP local protocol is disabled.  Note is value is independent of the `http` argument  **Choices:**   - `false` - `true` |
| **local_http_port**  integer | Configures the HTTP port that will listen for connections when the HTTP transport protocol is enabled. This argument accepts integer values in the valid range of 1 to 65535. |
| **socket**  aliases: enable_socket  boolean | The `socket` argument controls the operating state of the UNIX Domain Socket used to receive eAPI requests. When the value of this argument is set to True, the UDS will listen for eAPI requests. When the value is set to False, the UDS will not be available to handle requests. By default when eAPI is first configured, the UDS is disabled.  **Choices:**   - `false` - `true` |
| **state**  string | The `state` argument controls the operational state of eAPI on the remote device. When this argument is set to `started`, eAPI is enabled to receive requests and when this argument is `stopped`, eAPI is disabled and will not receive requests.  **Choices:**   - `"started"` ← (default) - `"stopped"` |
| **timeout**  integer | The time (in seconds) to wait for the eAPI configuration to be reflected in the running-config.  **Default:** `30` |
| **vrf**  string | The `vrf` argument will configure eAPI to listen for connections in the specified VRF. By default, eAPI transports will listen for connections in the global table. This value requires the VRF to already be created otherwise the task will fail.  **Default:** `"default"` |

## [Examples](eos_eapi_module.md#id4)

```yaml+jinja
- name: Enable eAPI access with default configuration
  arista.eos.eos_eapi:
    state: started

- name: Enable eAPI with no HTTP, HTTPS at port 9443, local HTTP at port 80, and socket
    enabled
  arista.eos.eos_eapi:
    state: started
    http: false
    https_port: 9443
    local_http: true
    local_http_port: 80
    socket: true

- name: Shutdown eAPI access
  arista.eos.eos_eapi:
    state: stopped
```

## [Return Values](eos_eapi_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["management api http-commands", "protocol http port 81", "no protocol https"]` |
| **session_name**  string | The EOS config session name used to load the configuration  **Returned:** when changed is True  **Sample:** `"ansible_1479315771"` |
| **urls**  dictionary | Hash of URL endpoints eAPI is listening on per interface  **Returned:** when eAPI is started  **Sample:** `{"Management1": ["http://172.26.10.1:80"]}` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
