---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_nac_policy module – Configure NAC policy matching pattern to identify matching NAC devices in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_nac_policy_module.html
fetched_at: 2026-07-27T17:46:01+00:00
---
# fortinet.fortios.fortios_user_nac_policy module – Configure NAC policy matching pattern to identify matching NAC devices in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_user_nac_policy_module.md#ansible-collections-fortinet-fortios-fortios-user-nac-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_nac_policy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_nac_policy_module.md#synopsis)
- [Requirements](fortios_user_nac_policy_module.md#requirements)
- [Parameters](fortios_user_nac_policy_module.md#parameters)
- [Notes](fortios_user_nac_policy_module.md#notes)
- [Examples](fortios_user_nac_policy_module.md#examples)
- [Return Values](fortios_user_nac_policy_module.md#return-values)

## [Synopsis](fortios_user_nac_policy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and nac_policy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_nac_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_nac_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_nac_policy**  dictionary | Configure NAC policy matching pattern to identify matching NAC devices. |
| **category**  string | Category of NAC policy.  Choices:   - `"device"` - `"firewall-user"` - `"ems-tag"` |
| **description**  string | Description for the NAC policy matching pattern. |
| **ems_tag**  string | NAC policy matching EMS tag. Source firewall.address.name. |
| **family**  string | NAC policy matching family. |
| **firewall_address**  string | Dynamic firewall address to associate MAC which match this policy. Source firewall.address.name. |
| **host**  string | NAC policy matching host. |
| **hw_vendor**  string | NAC policy matching hardware vendor. |
| **hw_version**  string | NAC policy matching hardware version. |
| **mac**  string | NAC policy matching MAC address. |
| **name**  string / required | NAC policy name. |
| **os**  string | NAC policy matching operating system. |
| **src**  string | NAC policy matching source. |
| **ssid_policy**  string | SSID policy to be applied on the matched NAC policy. Source wireless-controller.ssid-policy.name. |
| **status**  string | Enable/disable NAC policy.  Choices:   - `"enable"` - `"disable"` |
| **sw_version**  string | NAC policy matching software version. |
| **switch_auto_auth**  string | NAC device auto authorization when discovered and nac-policy matched.  Choices:   - `"global"` - `"disable"` - `"enable"` |
| **switch_fortilink**  string | FortiLink interface for which this NAC policy belongs to. Source system.interface.name. |
| **switch_group**  list / elements=dictionary | List of managed FortiSwitch groups on which NAC policy can be applied. |
| **name**  string | Managed FortiSwitch group name from available options. Source switch-controller.switch-group.name. |
| **switch_mac_policy**  string | Switch MAC policy action to be applied on the matched NAC policy. Source switch-controller.mac-policy.name. |
| **switch_port_policy**  string | switch-port-policy to be applied on the matched NAC policy. Source switch-controller.port-policy.name. |
| **switch_scope**  list / elements=dictionary | List of managed FortiSwitches on which NAC policy can be applied. |
| **switch_id**  string | Managed FortiSwitch name from available options. Source switch-controller.managed-switch.switch-id. |
| **type**  string | NAC policy matching type. |
| **user**  string | NAC policy matching user. |
| **user_group**  string | NAC policy matching user group. Source user.group.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_nac_policy_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_nac_policy_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure NAC policy matching pattern to identify matching NAC devices.
    fortios_user_nac_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_nac_policy:
        category: "device"
        description: "<your_own_value>"
        ems_tag: "<your_own_value> (source firewall.address.name)"
        family: "<your_own_value>"
        firewall_address: "<your_own_value> (source firewall.address.name)"
        host: "myhostname"
        hw_vendor: "<your_own_value>"
        hw_version: "<your_own_value>"
        mac: "<your_own_value>"
        name: "default_name_12"
        os: "<your_own_value>"
        src: "<your_own_value>"
        ssid_policy: "<your_own_value> (source wireless-controller.ssid-policy.name)"
        status: "enable"
        sw_version: "<your_own_value>"
        switch_auto_auth: "global"
        switch_fortilink: "<your_own_value> (source system.interface.name)"
        switch_group:
         -
            name: "default_name_21 (source switch-controller.switch-group.name)"
        switch_mac_policy: "<your_own_value> (source switch-controller.mac-policy.name)"
        switch_port_policy: "<your_own_value> (source switch-controller.port-policy.name)"
        switch_scope:
         -
            switch_id: "<your_own_value> (source switch-controller.managed-switch.switch-id)"
        type: "<your_own_value>"
        user: "<your_own_value>"
        user_group: "<your_own_value> (source user.group.name)"
```

## [Return Values](fortios_user_nac_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
