---
collection: ansible
version: "6"
title: "netbox.netbox.nb_lookup lookup – Queries and returns elements from NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/nb_lookup_lookup.html
fetched_at: 2026-07-27T16:43:33+00:00
---
# netbox.netbox.nb_lookup lookup – Queries and returns elements from NetBox

> **Note:**
>
> This lookup plugin is part of the [netbox.netbox collection](https://galaxy.ansible.com/netbox/netbox) (version 3.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](nb_lookup_lookup.md#ansible-collections-netbox-netbox-nb-lookup-lookup-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.nb_lookup`.

New in netbox.netbox 0.1.0

- [Synopsis](nb_lookup_lookup.md#synopsis)
- [Requirements](nb_lookup_lookup.md#requirements)
- [Terms](nb_lookup_lookup.md#terms)
- [Keyword parameters](nb_lookup_lookup.md#keyword-parameters)
- [Notes](nb_lookup_lookup.md#notes)
- [Examples](nb_lookup_lookup.md#examples)
- [Return Value](nb_lookup_lookup.md#return-value)

## [Synopsis](nb_lookup_lookup.md#id1)

- Queries NetBox via its API to return virtually any information capable of being held in NetBox.
- If wanting to obtain the plaintext attribute of a secret, *private_key* or *key_file* must be provided.

## [Requirements](nb_lookup_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- pynetbox

## [Terms](nb_lookup_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The NetBox object type to query |

## [Keyword parameters](nb_lookup_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('netbox.netbox.nb_lookup', key1=value1, key2=value2, ...)` and `query('netbox.netbox.nb_lookup', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string / required | The URL to the NetBox instance to query  Configuration:   - Environment variable: [`NETBOX_API`](../../environment_variables.md#envvar-NETBOX_API) - Environment variable: [`NETBOX_URL`](../../environment_variables.md#envvar-NETBOX_URL) |
| **api_filter**  string | The api_filter to use. Filters should be key value pairs separated by a space. |
| **key_file**  string | The location of the private key tied to user account. Mutually exclusive with *private_key*. |
| **plugin**  string | The NetBox plugin to query |
| **private_key**  string | The private key as a string. Mutually exclusive with *key_file*. |
| **raw_data**  boolean | Whether to return raw API data with the lookup/query or whether to return a key/value dict  Choices:   - `false` - `true` |
| **token**  string | The API token created through NetBox  This may not be required depending on the NetBox setup.  Configuration:   - Environment variable: [`NETBOX_TOKEN`](../../environment_variables.md#envvar-NETBOX_TOKEN) - Environment variable: [`NETBOX_API_TOKEN`](../../environment_variables.md#envvar-NETBOX_API_TOKEN) |
| **validate_certs**  string | Whether or not to validate SSL of the NetBox instance  Default: `true` |

## [Notes](nb_lookup_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('netbox.netbox.nb_lookup', term1, term2, key1=value1, key2=value2)` and `query('netbox.netbox.nb_lookup', term1, term2, key1=value1, key2=value2)`

## [Examples](nb_lookup_lookup.md#id6)

```yaml+jinja
tasks:
  # query a list of devices
  - name: Obtain list of devices from NetBox
    debug:
      msg: >
        "Device {{ item.value.display_name }} (ID: {{ item.key }}) was
         manufactured by {{ item.value.device_type.manufacturer.name }}"
    loop: "{{ query('netbox.netbox.nb_lookup', 'devices',
                    api_endpoint='http://localhost/',
                    token='<redacted>') }}"

# This example uses an API Filter

tasks:
  # query a list of devices
  - name: Obtain list of devices from NetBox
    debug:
      msg: >
        "Device {{ item.value.display_name }} (ID: {{ item.key }}) was
         manufactured by {{ item.value.device_type.manufacturer.name }}"
    loop: "{{ query('netbox.netbox.nb_lookup', 'devices',
                    api_endpoint='http://localhost/',
                    api_filter='role=management tag=Dell'),
                    token='<redacted>') }}"

# Obtain a secret for R1-device
tasks:
  - name: "Obtain secrets for R1-Device"
    debug:
      msg: "{{ query('netbox.netbox.nb_lookup', 'secrets', api_filter='device=R1-Device', api_endpoint='http://localhost/', token='<redacted>', key_file='~/.ssh/id_rsa') }}"

# Fetch bgp sessions for R1-device
tasks:
  - name: "Obtain bgp sessions for R1-Device"
    debug:
      msg: "{{ query('netbox.netbox.nb_lookup', 'bgp_sessions',
                     api_filter='device=R1-Device',
                     api_endpoint='http://localhost/',
                     token='<redacted>',
                     plugin='mycustomstuff') }}"

      msg: "{{ query('netbox.netbox.nb_lookup', 'secrets', api_filter='device=R1-Device', api_endpoint='http://localhost/', token='<redacted>', key_file='~/.ssh/id_rsa') }}"
```

## [Return Value](nb_lookup_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | list of composed dictionaries with key and value  Returned: success |

### Authors

- Chris Mills (@cpmills1975)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
