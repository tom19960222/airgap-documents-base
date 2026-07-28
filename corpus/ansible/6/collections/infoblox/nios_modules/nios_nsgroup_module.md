---
collection: ansible
version: "6"
title: "infoblox.nios_modules.nios_nsgroup module – Configure InfoBlox DNS Nameserver Groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infoblox/nios_modules/nios_nsgroup_module.html
fetched_at: 2026-07-27T17:51:02+00:00
---
# infoblox.nios_modules.nios_nsgroup module – Configure InfoBlox DNS Nameserver Groups

> **Note:**
>
> This module is part of the [infoblox.nios_modules collection](https://galaxy.ansible.com/infoblox/nios_modules) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infoblox.nios_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](nios_nsgroup_module.md#ansible-collections-infoblox-nios-modules-nios-nsgroup-module-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_nsgroup`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_nsgroup_module.md#synopsis)
- [Requirements](nios_nsgroup_module.md#requirements)
- [Parameters](nios_nsgroup_module.md#parameters)
- [Notes](nios_nsgroup_module.md#notes)
- [Examples](nios_nsgroup_module.md#examples)

## [Synopsis](nios_nsgroup_module.md#id1)

- Adds and/or removes nameserver groups form Infoblox NIOS servers. This module manages NIOS `nsgroup` objects using the Infoblox. WAPI interface over REST.

## [Requirements](nios_nsgroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- infoblox_client

## [Parameters](nios_nsgroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Configures a text string comment to be associated with the instance of this object. The provided text string will be configured on the object instance. |
| **extattrs**  string | Allows for the configuration of Extensible Attributes on the instance of the object. This argument accepts a set of key / value pairs for configuration. |
| **external_primaries**  list / elements=dictionary | Configures a list of external nameservers (non-members of the grid). This option is required when setting *use_external_primaries* to `true`. |
| **address**  string / required | Configures the IP address of the external nameserver |
| **name**  string / required | Set a label for the external nameserver |
| **stealth**  boolean | Configure the external nameserver as stealth server (without NS record) in the zones.  Choices:   - `false` ← (default) - `true` |
| **tsig_key**  string | Set a DNS TSIG key for the nameserver to secure zone transfers (AFXRs). |
| **tsig_key_alg**  string | Provides the algorithm used for the *tsig_key* in use.  Choices:   - `"HMAC-MD5"` ← (default) - `"HMAC-SHA256"` |
| **tsig_key_name**  string / required | Sets a label for the *tsig_key* value |
| **external_secondaries**  list / elements=dictionary | Allows to provide a list of external secondary nameservers, that are not members of the grid. |
| **address**  string / required | Configures the IP address of the external nameserver |
| **name**  string / required | Set a label for the external nameserver |
| **stealth**  boolean | Configure the external nameserver as stealth server (without NS record) in the zones.  Choices:   - `false` ← (default) - `true` |
| **tsig_key**  string | Set a DNS TSIG key for the nameserver to secure zone transfers (AFXRs). |
| **tsig_key_alg**  string | Provides the algorithm used for the *tsig_key* in use.  Choices:   - `"HMAC-MD5"` ← (default) - `"HMAC-SHA256"` |
| **tsig_key_name**  string / required | Sets a label for the *tsig_key* value |
| **grid_primary**  list / elements=dictionary | This host is to be used as primary server in this nameserver group. It must be a grid member. This option is required when setting *use_external_primaries* to `false`. |
| **enable_preferred_primaries**  boolean | This flag represents whether the preferred_primaries field values of this member are used (see Infoblox WAPI docs).  Choices:   - `false` ← (default) - `true` |
| **grid_replicate**  boolean | Use DNS zone transfers if set to `True` or ID Grid Replication if set to `False`.  Choices:   - `false` ← (default) - `true` |
| **lead**  boolean | This flag controls if the grid lead secondary nameserver performs zone transfers to non lead secondaries.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Provide the name of the grid member to identify the host. |
| **preferred_primaries**  list / elements=dictionary | Provide a list of elements like in *external_primaries* to set the precedence of preferred primary nameservers. |
| **address**  string / required | Configures the IP address of the external nameserver |
| **name**  string / required | Set a label for the external nameserver |
| **stealth**  boolean | Configure the external nameserver as stealth server (without NS record) in the zones.  Choices:   - `false` ← (default) - `true` |
| **tsig_key**  string | Set a DNS TSIG key for the nameserver to secure zone transfers (AFXRs). |
| **tsig_key_alg**  string | Provides the algorithm used for the *tsig_key* in use.  Choices:   - `"HMAC-MD5"` ← (default) - `"HMAC-SHA256"` |
| **tsig_key_name**  string / required | Sets a label for the *tsig_key* value |
| **stealth**  boolean | Configure the external nameserver as stealth server (without NS record) in the zones.  Choices:   - `false` ← (default) - `true` |
| **grid_secondaries**  list / elements=dictionary | Configures the list of grid member hosts that act as secondary nameservers. This option is required when setting *use_external_primaries* to `true`. |
| **enable_preferred_primaries**  boolean | This flag represents whether the preferred_primaries field values of this member are used (see Infoblox WAPI docs).  Choices:   - `false` ← (default) - `true` |
| **grid_replicate**  boolean | Use DNS zone transfers if set to `True` or ID Grid Replication if set to `False`  Choices:   - `false` ← (default) - `true` |
| **lead**  boolean | This flag controls if the grid lead secondary nameserver performs zone transfers to non lead secondaries.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Provide the name of the grid member to identify the host. |
| **preferred_primaries**  list / elements=dictionary | Provide a list of elements like in *external_primaries* to set the precedence of preferred primary nameservers. |
| **address**  string / required | Configures the IP address of the external nameserver |
| **name**  string / required | Set a label for the external nameserver |
| **stealth**  boolean | Configure the external nameserver as stealth server (without NS record) in the zones.  Choices:   - `false` ← (default) - `true` |
| **tsig_key**  string | Set a DNS TSIG key for the nameserver to secure zone transfers (AFXRs). |
| **tsig_key_alg**  string | Provides the algorithm used for the *tsig_key* in use.  Choices:   - `"HMAC-MD5"` ← (default) - `"HMAC-SHA256"` |
| **tsig_key_name**  string / required | Sets a label for the *tsig_key* value |
| **stealth**  boolean | Configure the external nameserver as stealth server (without NS record) in the zones.  Choices:   - `false` ← (default) - `true` |
| **is_grid_default**  boolean | If set to `True` this nsgroup will become the default nameserver group for new zones.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Specifies the name of the NIOS nameserver group to be managed. |
| **provider**  dictionary | A dict object containing connection details. |
| **cert**  string | Specifies the client certificate file with digest of x509 config for extra layer secure connection the remote instance of NIOS.  Value can also be specified using `INFOBLOX_CERT` environment variable. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST  Value can also be specified using `INFOBLOX_HOST` environment variable. |
| **http_pool_connections**  integer | Insert decription here  Default: `10` |
| **http_pool_maxsize**  integer | Insert description here  Default: `10` |
| **http_request_timeout**  integer | The amount of time before to wait before receiving a response  Value can also be specified using `INFOBLOX_HTTP_REQUEST_TIMEOUT` environment variable.  Default: `10` |
| **key**  string | Specifies private key file for encryption with the certificate in order to connect with remote instance of NIOS.  Value can also be specified using `INFOBLOX_KEY` environment variable. |
| **max_results**  integer | Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.  Value can also be specified using `INFOBLOX_MAX_RESULTS` environment variable.  Default: `1000` |
| **max_retries**  integer | Configures the number of attempted retries before the connection is declared usable  Value can also be specified using `INFOBLOX_MAX_RETRIES` environment variable.  Default: `3` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_PASSWORD` environment variable. |
| **silent_ssl_warnings**  boolean | Insert description here  Choices:   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_USERNAME` environment variable. |
| **validate_certs**  aliases: ssl_verify  boolean | Boolean value to enable or disable verifying SSL certificates  Value can also be specified using `INFOBLOX_SSL_VERIFY` environment variable.  Choices:   - `false` ← (default) - `true` |
| **wapi_version**  string | Specifies the version of WAPI to use  Value can also be specified using `INFOBLOX_WAP_VERSION` environment variable.  Until ansible 2.8 the default WAPI was 1.4  Default: `"2.1"` |
| **state**  string | Configures the intended state of the instance of the object on the NIOS server. When this value is set to `present`, the object is configured on the device and when this value is set to `absent` the value is removed (if necessary) from the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_external_primary**  boolean | This flag controls whether the group is using an external primary nameserver. Note that modification of this field requires passing values for *grid_secondaries* and *external_primaries*.  Choices:   - `false` ← (default) - `true` |

## [Notes](nios_nsgroup_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - This module must be run locally, which can be achieved by specifying `connection: local`.
> - Please read the :ref:`nios_guide` for more detailed information on how to use Infoblox with Ansible.

## [Examples](nios_nsgroup_module.md#id5)

```yaml+jinja
- name: Create simple infoblox nameserver group
  infoblox.nios_modules.nios_nsgroup:
    name: my-simple-group
    comment: "this is a simple nameserver group"
    grid_primary:
      - name: infoblox-test.example.com
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Create infoblox nameserver group with external primaries
  infoblox.nios_modules.nios_nsgroup:
    name: my-example-group
    use_external_primary: true
    comment: "this is my example nameserver group"
    external_primaries: "{{ ext_nameservers }}"
    grid_secondaries:
      - name: infoblox-test.example.com
        lead: True
        preferred_primaries: "{{ ext_nameservers }}"
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Delete infoblox nameserver group
  infoblox.nios_modules.nios_nsgroup:
    name: my-simple-group
    comment: "this is a simple nameserver group"
    grid_primary:
      - name: infoblox-test.example.com
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
```

### Authors

- Erich Birngruber (@ebirn)
- Sumit Jaiswal (@sjaiswal)

### Collection links

[Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
[Homepage](https://github.com/infobloxopen/infoblox-ansible)
[Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
