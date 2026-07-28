---
collection: ansible
version: "8"
title: "community.network.netscaler_save_config module – Save Netscaler configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/netscaler_save_config_module.html
fetched_at: 2026-07-28T01:57:10+00:00
---
# community.network.netscaler_save_config module – Save Netscaler configuration.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](netscaler_save_config_module.md#ansible-collections-community-network-netscaler-save-config-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_save_config`.

- [Synopsis](netscaler_save_config_module.md#synopsis)
- [Requirements](netscaler_save_config_module.md#requirements)
- [Parameters](netscaler_save_config_module.md#parameters)
- [Examples](netscaler_save_config_module.md#examples)
- [Return Values](netscaler_save_config_module.md#return-values)

## [Synopsis](netscaler_save_config_module.md#id1)

- This module unconditionally saves the configuration on the target netscaler node.
- This module does not support check mode.
- This module is intended to run either on the ansible control node or a bastion (jumpserver) with access to the actual netscaler instance.

Aliases: network.netscaler.netscaler_save_config

## [Requirements](netscaler_save_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_save_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  **Choices:**   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  string | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler.  **Default:** `310` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. `192.168.1.1:555`. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](netscaler_save_config_module.md#id4)

```yaml+jinja
---
- name: Save netscaler configuration
  delegate_to: localhost
  community.network.netscaler_save_config:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

- name: Setup server without saving  configuration
  delegate_to: localhost
  notify: Save configuration
  netscaler_server:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    save_config: false

    name: server-1
    ipaddress: 192.168.1.1

# Under playbook's handlers

- name: Save configuration
  delegate_to: localhost
  community.network.netscaler_save_config:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot
```

## [Return Values](netscaler_save_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **loglines**  list / elements=string | list of logged messages by the module  **Returned:** always  **Sample:** `["message 1", "message 2"]` |
| **msg**  string | Message detailing the failure reason  **Returned:** failure  **Sample:** `"Action does not exist"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
