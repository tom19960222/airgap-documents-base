---
collection: ansible
version: "8"
title: "community.network.pn_port_cos_rate_setting module – CLI command to modify port-cos-rate-setting"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_port_cos_rate_setting_module.html
fetched_at: 2026-07-28T01:57:32+00:00
---
# community.network.pn_port_cos_rate_setting module – CLI command to modify port-cos-rate-setting

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.pn_port_cos_rate_setting`.

- [Synopsis](pn_port_cos_rate_setting_module.md#synopsis)
- [Parameters](pn_port_cos_rate_setting_module.md#parameters)
- [Examples](pn_port_cos_rate_setting_module.md#examples)
- [Return Values](pn_port_cos_rate_setting_module.md#return-values)

## [Synopsis](pn_port_cos_rate_setting_module.md#id1)

- This modules can be used to update the port cos rate limit.

Aliases: network.netvisor.pn_port_cos_rate_setting

## [Parameters](pn_port_cos_rate_setting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_cos0_rate**  string | cos0 rate limit (pps) unlimited or 0 to 10000000. |
| **pn_cos1_rate**  string | cos1 rate limit (pps) unlimited or 0 to 10000000. |
| **pn_cos2_rate**  string | cos2 rate limit (pps) unlimited or 0 to 10000000. |
| **pn_cos3_rate**  string | cos3 rate limit (pps) unlimited or 0 to 10000000. |
| **pn_cos4_rate**  string | cos4 rate limit (pps) unlimited or 0 to 10000000. |
| **pn_cos5_rate**  string | cos5 rate limit (pps) unlimited or 0 to 10000000. |
| **pn_cos6_rate**  string | cos6 rate limit (pps) unlimited or 0 to 10000000. |
| **pn_cos7_rate**  string | cos7 rate limit (pps) unlimited or 0 to 10000000. |
| **pn_port**  string | port.  **Choices:**   - `"control-port"` - `"data-port"` - `"span-ports"` |
| **state**  string / required | State the action to perform. Use `update` to modify the port-cos-rate-setting.  **Choices:**   - `"update"` |

## [Examples](pn_port_cos_rate_setting_module.md#id3)

```yaml+jinja
- name: Port cos rate modify
  community.network.pn_port_cos_rate_setting:
    pn_cliswitch: "sw01"
    state: "update"
    pn_port: "control-port"
    pn_cos1_rate: "1000"
    pn_cos5_rate: "1000"
    pn_cos2_rate: "1000"
    pn_cos0_rate: "1000"

- name: Port cos rate modify
  community.network.pn_port_cos_rate_setting:
    pn_cliswitch: "sw01"
    state: "update"
    pn_port: "data-port"
    pn_cos1_rate: "2000"
    pn_cos5_rate: "2000"
    pn_cos2_rate: "2000"
    pn_cos0_rate: "2000"
```

## [Return Values](pn_port_cos_rate_setting_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the port-cos-rate-setting command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the port-cos-rate-setting command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
