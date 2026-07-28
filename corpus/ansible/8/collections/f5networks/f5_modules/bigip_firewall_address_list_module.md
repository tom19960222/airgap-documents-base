---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_firewall_address_list module – Manage address lists on BIG-IP AFM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_firewall_address_list_module.html
fetched_at: 2026-07-28T02:06:04+00:00
---
# f5networks.f5_modules.bigip_firewall_address_list module – Manage address lists on BIG-IP AFM

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_firewall_address_list`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_firewall_address_list_module.md#synopsis)
- [Parameters](bigip_firewall_address_list_module.md#parameters)
- [Notes](bigip_firewall_address_list_module.md#notes)
- [Examples](bigip_firewall_address_list_module.md#examples)
- [Return Values](bigip_firewall_address_list_module.md#return-values)

## [Synopsis](bigip_firewall_address_list_module.md#id1)

- Manages the AFM (Advanced Firewall Manager) address lists on a BIG-IP. This module can be used to add and remove address list entries.

## [Parameters](bigip_firewall_address_list_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address_lists**  list / elements=string | Simple list of existing address lists to add to this list. Address lists can be specified in either their fully qualified name (/Common/foo) or their short name (foo). If a short name is used, the `partition` argument will automatically be prepended to the short name. |
| **address_ranges**  list / elements=string | A list of address ranges where the range starts with a port number, is followed by a dash (-), and then a second number.  If the first address is greater than the second number, the numbers will be reversed so they are properly formatted. For example, `2.2.2.2-1.1.1`. would become `1.1.1.1-2.2.2.2`. |
| **addresses**  list / elements=string | Individual addresses you want to add to the list. These addresses differ from ranges and lists of lists, such as what can be used in `address_ranges` and `address_lists` respectively.  This list can also include networks that have CIDR notation. |
| **description**  string | Description of the address list. |
| **fqdns**  list / elements=string | A list of fully qualified domain names (FQDNs).  An FQDN has at least one decimal point in it, separating the host from the domain.  To add FQDNs to a list requires that a global FQDN resolver is configured. This must be done using `bigip_command` or from the GUI of the BIG-IP. If using `bigip_command`, you can do this with `tmsh modify security firewall global-fqdn-policy FOO` where `FOO` is a DNS resolver configured at `tmsh create net dns-resolver FOO`. |
| **geo_locations**  list / elements=dictionary | List of geolocations specified by their `country` and `region`. |
| **country**  string / required | The country name or code of the geolocation to use.  In addition to the country full names, you may also specify their abbreviated form, such as `US` instead of `United States`.  Valid country codes can be found here <https://countrycode.org/>. |
| **region**  string | Region name of the country to use. |
| **name**  string / required | Specifies the name of the address list. |
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
| **state**  string | When `present`, ensures the address list and entries exists.  When `absent`, ensures the address list is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_firewall_address_list_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_firewall_address_list_module.md#id4)

```yaml+jinja
- name: Create an address list
  bigip_firewall_address_list:
    name: foo
    addresses:
      - 3.3.3.3
      - 4.4.4.4
      - 5.5.5.5
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_firewall_address_list_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address_lists**  list / elements=string | The new list of address list names applied to the address list.  **Returned:** changed  **Sample:** `["/Common/list1", "/Common/list2"]` |
| **address_ranges**  list / elements=string | The new list of address ranges applied to the address list.  **Returned:** changed  **Sample:** `["1.1.1.1-2.2.2.2", "3.3.3.3-4.4.4.4"]` |
| **addresses**  list / elements=string | The new list of addresses applied to the address list.  **Returned:** changed  **Sample:** `["1.1.1.1", "2.2.2.2"]` |
| **description**  string | The new description of the address list.  **Returned:** changed  **Sample:** `"My address list"` |
| **fqdns**  list / elements=string | The new list of FQDN names applied to the address list.  **Returned:** changed  **Sample:** `["google.com", "mit.edu"]` |
| **geo_locations**  complex | The new list of geolocations applied to the address list.  **Returned:** changed |
| **country**  string | Country of the geolocation.  **Returned:** changed  **Sample:** `"US"` |
| **region**  string | Region of the geolocation.  **Returned:** changed  **Sample:** `"California"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
