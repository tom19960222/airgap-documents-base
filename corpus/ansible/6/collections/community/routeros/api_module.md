---
collection: ansible
version: "6"
title: "community.routeros.api module – Ansible module for RouterOS API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/routeros/api_module.html
fetched_at: 2026-07-27T17:20:51+00:00
---
# community.routeros.api module – Ansible module for RouterOS API

> **Note:**
>
> This module is part of the [community.routeros collection](https://galaxy.ansible.com/community/routeros) (version 2.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.routeros`.
> You need further requirements to be able to use this module,
> see [Requirements](api_module.md#ansible-collections-community-routeros-api-module-requirements) for details.
>
> To use it in a playbook, specify: `community.routeros.api`.

- [Synopsis](api_module.md#synopsis)
- [Requirements](api_module.md#requirements)
- [Parameters](api_module.md#parameters)
- [Attributes](api_module.md#attributes)
- [Notes](api_module.md#notes)
- [See Also](api_module.md#see-also)
- [Examples](api_module.md#examples)
- [Return Values](api_module.md#return-values)

## [Synopsis](api_module.md#id1)

- Ansible module for RouterOS API with the Python `librouteros` library.
- This module can add, remove, update, query and execute arbitrary command in RouterOS via API.

## [Requirements](api_module.md#id2)

The below requirements are needed on the host that executes this module.

- librouteros
- Python >= 3.6 (for librouteros)

## [Parameters](api_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add**  string | Will add selected arguments in selected path to RouterOS config.  Example `address=1.1.1.1/32 interface=ether1`.  Equivalent in RouterOS CLI `/ip address add address=1.1.1.1/32 interface=ether1`. |
| **ca_path**  path  added in community.routeros 1.2.0 | PEM formatted file that contains a CA certificate to be used for certificate validation.  See also *validate_cert_hostname*. Only used when *tls=true* and *validate_certs=true*. |
| **cmd**  string | Execute any/arbitrary command in selected path, after the command we can add `.id`.  Example path `system script` and cmd `run .id=*03` is equivalent in RouterOS CLI `/system script run number=0`.  Example path `ip address` and cmd `print` is equivalent in RouterOS CLI `/ip address print`. |
| **encoding**  string  added in community.routeros 2.1.0 | Use the specified encoding when communicating with the RouterOS device.  Default is `ASCII`. Note that `UTF-8` requires librouteros 3.2.1 or newer.  Default: `"ASCII"` |
| **extended_query**  dictionary | Extended query given path for selected query attributes from RouterOS API.  Extended query allow conjunctive input. If there is no matching entry, an empty list will be returned. |
| **attributes**  list / elements=string / required | The list of attributes to return.  Every attribute used in a *where* clause need to be listed here. |
| **where**  list / elements=dictionary | Allows to restrict the objects returned.  The conditions here must all match. An *or* condition needs at least one of its conditions to match. |
| **attribute**  string | The attribute to match. Must be part of *attributes*.  Either *or* or all of *attribute*, *is*, and *value* have to be specified. |
| **is**  string | The operator to use for matching.  For equality use `==` or `eq`. For less use `<` or `less`. For more use `>` or `more`.  Use `in` to check whether the value is part of a list. In that case, *value* must be a list.  Either *or* or all of *attribute*, *is*, and *value* have to be specified.  Choices:   - `"=="` - `"!="` - `">"` - `"<"` - `"in"` - `"eq"` - `"not"` - `"more"` - `"less"` |
| **or**  list / elements=dictionary | A list of conditions so that at least one of them has to match.  Either *or* or all of *attribute*, *is*, and *value* have to be specified. |
| **attribute**  string / required | The attribute to match. Must be part of *attributes*. |
| **is**  string / required | The operator to use for matching.  For equality use `==` or `eq`. For less use `<` or `less`. For more use `>` or `more`.  Use `in` to check whether the value is part of a list. In that case, *value* must be a list.  Choices:   - `"=="` - `"!="` - `">"` - `"<"` - `"in"` - `"eq"` - `"not"` - `"more"` - `"less"` |
| **value**  any / required | The value to compare to. Must be a list for *is=in*. |
| **value**  any | The value to compare to. Must be a list for *is=in*.  Either *or* or all of *attribute*, *is*, and *value* have to be specified. |
| **force_no_cert**  boolean  added in community.routeros 2.4.0 | Set to `true` to connect without a certificate when *tls=true*.  See also *validate_certs*.  **Note:** this forces the use of anonymous Diffie-Hellman (ADH) ciphers. The protocol is susceptible to Man-in-the-Middle attacks, because the keys used in the exchange are not authenticated. Instead of simply connecting without a certificate to “make things work” have a look at *validate_certs* and *ca_path*.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string / required | RouterOS hostname API. |
| **password**  string / required | RouterOS user password. |
| **path**  string / required | Main path for all other arguments.  If other arguments are not set, api will return all items in selected path.  Example `ip address`. Equivalent of RouterOS CLI `/ip address print`. |
| **port**  integer | RouterOS api port. If *tls* is set, port will apply to TLS/SSL connection.  Defaults are `8728` for the HTTP API, and `8729` for the HTTPS API. |
| **query**  string | Query given path for selected query attributes from RouterOS aip.  WHERE is key word which extend query. WHERE format is key operator value - with spaces.  WHERE valid operators are `==` or `eq`, `!=` or `not`, `>` or `more`, `<` or `less`.  Example path `ip address` and query `.id address` will return only `.id` and `address` for all items in `ip address` path.  Example path `ip address` and query `.id address WHERE address == 1.1.1.3/32`. will return only `.id` and `address` for items in `ip address` path, where address is eq to 1.1.1.3/32.  Example path `interface` and query `mtu name WHERE mut > 1400` will return only interfaces `mtu,name` where mtu is bigger than 1400.  Equivalent in RouterOS CLI `/interface print where mtu > 1400`. |
| **remove**  string | Remove config/value from RouterOS by ‘.id’.  Example `*03` will remove config/value with `id=*03` in selected path.  Equivalent in RouterOS CLI `/ip address remove numbers=1`.  Note `number` in RouterOS CLI is different from `.id`. |
| **timeout**  integer  added in community.routeros 2.3.0 | Timeout for the request.  Default: `10` |
| **tls**  aliases: ssl  boolean | If is set TLS will be used for RouterOS API connection.  Choices:   - `false` ← (default) - `true` |
| **update**  string | Update config/value in RouterOS by ‘.id’ in selected path.  Example `.id=*03 address=1.1.1.3/32` and path `ip address` will replace existing ip address with `.id=*03`.  Equivalent in RouterOS CLI `/ip address set address=1.1.1.3/32 numbers=1`.  Note `number` in RouterOS CLI is different from `.id`. |
| **username**  string / required | RouterOS login user. |
| **validate_cert_hostname**  boolean  added in community.routeros 1.2.0 | Set to `true` to validate hostnames in certificates.  See also *validate_certs*. Only used when *tls=true* and *validate_certs=true*.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean  added in community.routeros 1.2.0 | Set to `false` to skip validation of TLS certificates.  See also *validate_cert_hostname*. Only used when *tls=true*.  **Note:** instead of simply deactivating certificate validations to “make things work”, please consider creating your own CA certificate and using it to sign certificates used for your router. You can tell the module about your CA certificate with the *ca_path* option.  Choices:   - `false` - `true` ← (default) |

## [Attributes](api_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.routeros.api  added in community.routeros 2.1.0 | Use `group/community.routeros.api` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: none | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **platform** | Platform: RouterOS | Target OS/families that can be operated against. |

## [Notes](api_module.md#id5)

> **Note:**
>
> - *add*, *remove*, *update*, *cmd* and *query* are mutually exclusive.
> - Use the [community.routeros.api_modify](api_modify_module.md#ansible-collections-community-routeros-api-modify-module) and [community.routeros.api_find_and_modify](api_find_and_modify_module.md#ansible-collections-community-routeros-api-find-and-modify-module) modules for more specific modifications, and the [community.routeros.api_info](api_info_module.md#ansible-collections-community-routeros-api-info-module) module for a more controlled way of returning all entries for a path.

## [See Also](api_module.md#id6)

> **See also:**
>
> [How to quote and unquote commands and arguments](docsite/quoting.md#ansible-collections-community-routeros-docsite-quoting)
> :   How to quote and unquote commands and arguments
>
> [community.routeros.api_facts](api_facts_module.md#ansible-collections-community-routeros-api-facts-module)
> :   Collect facts from remote devices running MikroTik RouterOS using the API.
>
> [community.routeros.api_find_and_modify](api_find_and_modify_module.md#ansible-collections-community-routeros-api-find-and-modify-module)
> :   Find and modify information using the API.
>
> [community.routeros.api_info](api_info_module.md#ansible-collections-community-routeros-api-info-module)
> :   Retrieve information from API.
>
> [community.routeros.api_modify](api_modify_module.md#ansible-collections-community-routeros-api-modify-module)
> :   Modify data at paths with API.
>
> [How to connect to RouterOS devices with the RouterOS API](docsite/api-guide.md#ansible-collections-community-routeros-docsite-api-guide)
> :   How to connect to RouterOS devices with the RouterOS API

## [Examples](api_module.md#id7)

```yaml+jinja
- name: Get example - ip address print
  community.routeros.api:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: "ip address"
  register: ipaddrd_printout

- name: Dump "Get example" output
  ansible.builtin.debug:
    msg: '{{ ipaddrd_printout }}'

- name: Add example - ip address
  community.routeros.api:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: "ip address"
    add: "address=192.168.255.10/24 interface=ether2"

- name: Query example - ".id, address" in "ip address WHERE address == 192.168.255.10/24"
  community.routeros.api:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: "ip address"
    query: ".id address WHERE address == {{ ip2 }}"
  register: queryout

- name: Dump "Query example" output
  ansible.builtin.debug:
    msg: '{{ queryout }}'

- name: Extended query example - ".id,address,network" where address is not 192.168.255.10/24 or is 10.20.36.20/24
  community.routeros.api:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: "ip address"
    extended_query:
      attributes:
        - network
        - address
        - .id
      where:
        - attribute: "network"
          is: "=="
          value: "192.168.255.0"
        - or:
            - attribute: "address"
              is: "!="
              value: "192.168.255.10/24"
            - attribute: "address"
              is: "eq"
              value: "10.20.36.20/24"
        - attribute: "network"
          is: "in"
          value:
             - "10.20.36.0"
             - "192.168.255.0"
  register: extended_queryout

- name: Dump "Extended query example" output
  ansible.builtin.debug:
    msg: '{{ extended_queryout }}'

- name: Update example - ether2 ip addres with ".id = *14"
  community.routeros.api:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: "ip address"
    update: >-
        .id=*14
        address=192.168.255.20/24
        comment={{ 'Update 192.168.255.10/24 to 192.168.255.20/24 on ether2' | community.routeros.quote_argument_value }}

- name: Remove example - ether2 ip 192.168.255.20/24 with ".id = *14"
  community.routeros.api:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: "ip address"
    remove: "*14"

- name: Arbitrary command example "/system identity print"
  community.routeros.api:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: "system identity"
    cmd: "print"
  register: arbitraryout

- name: Dump "Arbitrary command example" output
  ansible.builtin.debug:
    msg: '{{ arbitraryout }}'
```

## [Return Values](api_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **message**  list / elements=string | All outputs are in list with dictionary elements returned from RouterOS api.  Returned: always  Sample: `[{"address": "1.2.3.4"}, {"address": "2.3.4.5"}]` |

### Authors

- Nikolay Dachev (@NikolayDachev)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.routeros)
[Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-routeros)
