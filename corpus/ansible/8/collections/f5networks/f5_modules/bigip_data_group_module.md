---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_data_group module – Manage data groups on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_data_group_module.html
fetched_at: 2026-07-28T02:05:46+00:00
---
# f5networks.f5_modules.bigip_data_group module – Manage data groups on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_data_group`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_data_group_module.md#synopsis)
- [Parameters](bigip_data_group_module.md#parameters)
- [Notes](bigip_data_group_module.md#notes)
- [Examples](bigip_data_group_module.md#examples)

## [Synopsis](bigip_data_group_module.md#id1)

- Allows for managing data groups on a BIG-IP. Data groups provide a way to store collections of values on a BIG-IP for later use in things such as LTM rules, iRules, and ASM policies.

## [Parameters](bigip_data_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **delete_data_group_file**  boolean | When `true`, ensures the remote data group file is deleted.  This parameter is only relevant when `state` is `absent` and `internal` is `false`.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | The description of the data group. |
| **external_file_name**  string | When creating a new data group, this specifies the file name you want to give an external data group file on the BIG-IP.  This parameter is ignored when `internal` is `true`.  This parameter can be used to select an existing data group file to use with an existing external data group.  If this value is not provided, it will be given the value specified in `name` and, therefore, match the name of the data group.  This value may only contain letters, numbers, underscores, dashes, or a period. |
| **internal**  boolean | The type of this data group.  You should only consider setting this value in cases where you know exactly what you are doing, **or**, you are working with a pre-existing internal data group.  Be aware that if you deliberately force this parameter to `true`, and you have a either a large number of records or a large total records size, this large amount of data will be reflected in your BIG-IP configuration. This can lead to **long** system configuration load times due to parsing and verifying the large configuration.  When this parameter is `true`, there is a limit for uploads of either 4 megabytes or 65,000 records, whichever is more restrictive.  This value cannot be changed once the data group is created.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Specifies the name of the data group. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **records**  list / elements=any | Specifies the records you want to add to a data group.  If you have a large number of records, we recommend you use `records_src` instead of typing all those records here.  The technical limit of either the number of records, or the total size of all records. Varies with the size of the total resources on your system; in particular, RAM.  When `internal` is `false`, at least one record must be specified in either `records` or `records_src`.  When `type` is: `ip`, `address`, `addr` if the addresses use a non-default route domain, they must be explicit about it, meaning they must contain a route domain notation `%` e.g. 10.10.1.1%11. This is true regardless if the data group resides in a partition or not. |
| **key**  string / required | The key describing the record in the data group.  The key will be used for validation of the `type` parameter to this module. |
| **value**  any | The value of the key describing the record in the data group. |
| **records_src**  path | Path to a file with records in it.  The file should be well-formed. This means it includes records, one per line, that resemble the following format “key separator value”. For example, `foo := bar`.  BIG-IP is strict about this format, but this module is a bit more lax. It will allow you to include arbitrary amounts (including none) of empty space on either side of the separator. For an illustration of this, see the Examples section.  Record keys are limited in length to no more than 65520 characters.  Values of record keys are limited in length to no more than 65520 characters.  The total number of records you can have in your BIG-IP is limited by the memory of the BIG-IP itself.  The format of this content is slightly different depending on whether you specify a `type` of `address`, `integer`, or `string`. See the examples section for examples of the different types of payload formats that are expected in your data group file.  When `internal` is `false`, at least one record must be specified in either `records` or `records_src`. |
| **separator**  string | When specifying `records_src`, this is the string of characters that will be used to break apart entries in the `records_src` into key/value pairs.  By default, the value of this parameter is `:=`.  This value cannot be changed once it is set.  This parameter is only relevant when `internal` is `false`. It will be ignored otherwise.  **Default:** `":="` |
| **state**  string | When `state` is `present`, ensures the data group exists.  When `state` is `absent`, ensures the data group is removed.  The use of state in this module refers to the entire data group, not its members.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | The type of records in this data group.  This parameter is important because it causes the BIG-IP to store your data in different ways to optimize access to it. For example, it would be wrong to specify a list of records containing IP addresses, but label them as a `string` type.  This value cannot be changed once the data group is created.  **Choices:**   - `"address"` - `"addr"` - `"ip"` - `"string"` ← (default) - `"integer"` - `"int"` |

## [Notes](bigip_data_group_module.md#id3)

> **Note:**
>
> - This module does NOT support atomic updates of data group members in a type `internal` data group.
> - Addition/Deletion of data group members in a type `external` data group should be done through Ansible modules only, if changes are made manually, the Ansible module will not detect those changes.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_data_group_module.md#id4)

```yaml+jinja
- name: Create a data group of addresses
  bigip_data_group:
    name: foo
    internal: true
    records:
      - key: 0.0.0.0/32
        value: External_NAT
      - key: 10.10.10.10
        value: No_NAT
    type: address
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a data group of strings
  bigip_data_group:
    name: foo
    internal: true
    records:
      - key: caddy
        value: ""
      - key: cafeteria
        value: ""
      - key: cactus
        value: ""
    type: string
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a data group of IP addresses from a file
  bigip_data_group:
    name: foo
    records_src: /path/to/dg-file
    type: address
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Update an existing internal data group of strings
  bigip_data_group:
    name: foo
    internal: true
    records:
      - key: caddy
        value: ""
      - key: cafeteria
        value: ""
      - key: cactus
        value: ""
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Show the data format expected for records_content - address 1
  copy:
    dest: /path/to/addresses.txt
    content: |
      network 10.0.0.0 prefixlen 8 := "Network1",
      network 172.16.0.0 prefixlen 12 := "Network2",
      network 192.168.0.0 prefixlen 16 := "Network3",
      network 2402:9400:1000:0:: prefixlen 64 := "Network4",
      host 192.168.20.1 := "Host1",
      host 172.16.1.1 := "Host2",
      host 172.16.1.1 := "Host3",
      host 2001:0db8:85a3:0000:0000:8a2e:0370:7334 := "Host4",
      host 2001:0db8:85a3:0000:0000:8a2e:0370:7334 := "Host5"

- name: Show the data format expected for records_content - address 2
  copy:
    dest: /path/to/addresses.txt
    content: |
      10.0.0.0/8 := "Network1",
      172.16.0.0/12 := "Network2",
      192.168.0.0/16 := "Network3",
      2402:9400:1000:0::/64 := "Network4",
      192.168.20.1 := "Host1",
      172.16.1.1 := "Host2",
      172.16.1.1/32 := "Host3",
      2001:0db8:85a3:0000:0000:8a2e:0370:7334 := "Host4",
      2001:0db8:85a3:0000:0000:8a2e:0370:7334/128 := "Host5"

- name: Show the data format expected for records_content - string
  copy:
    dest: /path/to/strings.txt
    content: |
      a := alpha,
      b := bravo,
      c := charlie,
      x := x-ray,
      y := yankee,
      z := zulu,

- name: Show the data format expected for records_content - integer
  copy:
    dest: /path/to/integers.txt
    content: |
      1 := bar,
      2 := baz,
      3,
      4,
```

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)
- Greg Crosby (@crosbygw)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
