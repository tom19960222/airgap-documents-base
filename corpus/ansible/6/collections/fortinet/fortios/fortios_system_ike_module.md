---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_ike module – Configure IKE global attributes in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_ike_module.html
fetched_at: 2026-07-27T17:44:39+00:00
---
# fortinet.fortios.fortios_system_ike module – Configure IKE global attributes in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_ike_module.md#ansible-collections-fortinet-fortios-fortios-system-ike-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_ike`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_ike_module.md#synopsis)
- [Requirements](fortios_system_ike_module.md#requirements)
- [Parameters](fortios_system_ike_module.md#parameters)
- [Notes](fortios_system_ike_module.md#notes)
- [Examples](fortios_system_ike_module.md#examples)
- [Return Values](fortios_system_ike_module.md#return-values)

## [Synopsis](fortios_system_ike_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and ike category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_ike_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_ike_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **system_ike**  dictionary | Configure IKE global attributes. |
| **dh_group_1**  dictionary | Diffie-Hellman group 1 (MODP-768). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_14**  dictionary | Diffie-Hellman group 14 (MODP-2048). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_15**  dictionary | Diffie-Hellman group 15 (MODP-3072). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_16**  dictionary | Diffie-Hellman group 16 (MODP-4096). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_17**  dictionary | Diffie-Hellman group 17 (MODP-6144). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_18**  dictionary | Diffie-Hellman group 18 (MODP-8192). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_19**  dictionary | Diffie-Hellman group 19 (EC-P256). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_2**  dictionary | Diffie-Hellman group 2 (MODP-1024). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_20**  dictionary | Diffie-Hellman group 20 (EC-P384). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_21**  dictionary | Diffie-Hellman group 21 (EC-P521). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_27**  dictionary | Diffie-Hellman group 27 (EC-P224BP). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_28**  dictionary | Diffie-Hellman group 28 (EC-P256BP). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_29**  dictionary | Diffie-Hellman group 29 (EC-P384BP). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_30**  dictionary | Diffie-Hellman group 30 (EC-P512BP). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_31**  dictionary | Diffie-Hellman group 31 (EC-X25519). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_32**  dictionary | Diffie-Hellman group 32 (EC-X448). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_group_5**  dictionary | Diffie-Hellman group 5 (MODP-1536). |
| **keypair_cache**  string | Configure custom key pair cache size for this Diffie-Hellman group.  Choices:   - `"global"` - `"custom"` |
| **keypair_count**  integer | Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker). |
| **mode**  string | Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.  Choices:   - `"software"` - `"hardware"` - `"global"` |
| **dh_keypair_cache**  string | Enable/disable Diffie-Hellman key pair cache.  Choices:   - `"enable"` - `"disable"` |
| **dh_keypair_count**  integer | Number of key pairs to pre-generate for each Diffie-Hellman group (per-worker). |
| **dh_keypair_throttle**  string | Enable/disable Diffie-Hellman key pair cache CPU throttling.  Choices:   - `"enable"` - `"disable"` |
| **dh_mode**  string | Use software (CPU) or hardware (CPX) to perform Diffie-Hellman calculations.  Choices:   - `"software"` - `"hardware"` |
| **dh_multiprocess**  string | Enable/disable multiprocess Diffie-Hellman daemon for IKE.  Choices:   - `"enable"` - `"disable"` |
| **dh_worker_count**  integer | Number of Diffie-Hellman workers to start. |
| **embryonic_limit**  integer | Maximum number of IPsec tunnels to negotiate simultaneously. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_ike_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_ike_module.md#id5)

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
  - name: Configure IKE global attributes.
    fortios_system_ike:
      vdom:  "{{ vdom }}"
      system_ike:
        dh_group_1:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_14:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_15:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_16:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_17:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_18:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_19:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_2:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_20:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_21:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_27:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_28:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_29:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_30:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_31:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_32:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_group_5:
            keypair_cache: "global"
            keypair_count: "0"
            mode: "software"
        dh_keypair_cache: "enable"
        dh_keypair_count: "100"
        dh_keypair_throttle: "enable"
        dh_mode: "software"
        dh_multiprocess: "enable"
        dh_worker_count: "0"
        embryonic_limit: "10000"
```

## [Return Values](fortios_system_ike_module.md#id6)

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
