---
collection: ansible
version: "8"
title: "community.network.ce_netconf module – Run an arbitrary netconf command on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_netconf_module.html
fetched_at: 2026-07-28T01:55:42+00:00
---
# community.network.ce_netconf module – Run an arbitrary netconf command on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_netconf`.

- [Synopsis](ce_netconf_module.md#synopsis)
- [Parameters](ce_netconf_module.md#parameters)
- [Notes](ce_netconf_module.md#notes)
- [Examples](ce_netconf_module.md#examples)
- [Return Values](ce_netconf_module.md#return-values)

## [Synopsis](ce_netconf_module.md#id1)

- Sends an arbitrary netconf command on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_netconf

## [Parameters](ce_netconf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cfg_xml**  string / required | The config xml string. |
| **rpc**  string / required | The type of rpc.  **Choices:**   - `"get"` - `"edit-config"` - `"execute-action"` - `"execute-cli"` |

## [Notes](ce_netconf_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_netconf_module.md#id4)

```yaml+jinja
- name: CloudEngine netconf test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:

  - name: "Netconf get operation"
    community.network.ce_netconf:
      rpc: get
      cfg_xml: '<filter type="subtree">
                  <vlan xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
                    <vlans>
                      <vlan>
                        <vlanId>10</vlanId>
                        <vlanif>
                          <ifName></ifName>
                          <cfgBand></cfgBand>
                          <dampTime></dampTime>
                        </vlanif>
                      </vlan>
                    </vlans>
                  </vlan>
                </filter>'

  - name: "Netconf edit-config operation"
    community.network.ce_netconf:
      rpc: edit-config
      cfg_xml: '<config>
                    <aaa xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
                      <authenticationSchemes>
                        <authenticationScheme operation="create">
                          <authenSchemeName>default_wdz</authenSchemeName>
                          <firstAuthenMode>local</firstAuthenMode>
                          <secondAuthenMode>invalid</secondAuthenMode>
                        </authenticationScheme>
                      </authenticationSchemes>
                    </aaa>
                   </config>'

  - name: "Netconf execute-action operation"
    community.network.ce_netconf:
      rpc: execute-action
      cfg_xml: '<action>
                     <l2mc xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
                       <l2McResetAllVlanStatis>
                         <addrFamily>ipv4unicast</addrFamily>
                       </l2McResetAllVlanStatis>
                     </l2mc>
                   </action>'
```

## [Return Values](ce_netconf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"result": ["ok"]}` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
