---
collection: ansible
version: "8"
title: "community.network.netscaler_cs_policy module – Manage content switching policy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/netscaler_cs_policy_module.html
fetched_at: 2026-07-28T01:57:04+00:00
---
# community.network.netscaler_cs_policy module – Manage content switching policy

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
> see [Requirements](netscaler_cs_policy_module.md#ansible-collections-community-network-netscaler-cs-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_cs_policy`.

- [Synopsis](netscaler_cs_policy_module.md#synopsis)
- [Requirements](netscaler_cs_policy_module.md#requirements)
- [Parameters](netscaler_cs_policy_module.md#parameters)
- [Notes](netscaler_cs_policy_module.md#notes)
- [Examples](netscaler_cs_policy_module.md#examples)
- [Return Values](netscaler_cs_policy_module.md#return-values)

## [Synopsis](netscaler_cs_policy_module.md#id1)

- Manage content switching policy.
- This module is intended to run either on the ansible control node or a bastion (jumpserver) with access to the actual netscaler instance.

Aliases: network.netscaler.netscaler_cs_policy

## [Requirements](netscaler_cs_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_cs_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | Content switching action that names the target load balancing virtual server to which the traffic is switched. |
| **domain**  string | The domain name. The string value can range to 63 characters.  Minimum length = 1 |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  **Choices:**   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  **Default:** `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **policyname**  string | Name for the content switching policy. Must begin with an ASCII alphanumeric or underscore `_` character, and must contain only ASCII alphanumeric, underscore, hash `#`, period `.`, space , colon `:`, at sign `@`, equal sign `=`, and hyphen `-` characters. Cannot be changed after a policy is created.  The following requirement applies only to the NetScaler CLI:  If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, my policy or my policy).  Minimum length = 1 |
| **rule**  string | Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.  Note:  Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: ‘”<string of 255 characters>” + “<string of 245 characters>”’ |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **url**  string | URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the string value in the following format: `[[prefix] [*]] [.suffix]`.  Minimum length = 1  Maximum length = 208 |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](netscaler_cs_policy_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_cs_policy_module.md#id5)

```yaml+jinja
- name: Create url cs policy
  delegate_to: localhost
  community.network.netscaler_cs_policy:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot
    validate_certs: false

    state: present

    policyname: policy_1
    url: /example/
```

## [Return Values](netscaler_cs_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  dictionary | List of differences between the actual configured object and the configuration specified in the module  **Returned:** failure  **Sample:** `{"url": "difference. ours: (str) example1 other: (str) /example1"}` |
| **loglines**  list / elements=string | list of logged messages by the module  **Returned:** always  **Sample:** `["message 1", "message 2"]` |
| **msg**  string | Message detailing the failure reason  **Returned:** failure  **Sample:** `"Could not load nitro python sdk"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
