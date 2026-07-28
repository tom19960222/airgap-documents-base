---
collection: ansible
version: "8"
title: "infoblox.nios_modules.nios_txt_record module – Configure Infoblox NIOS txt records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/infoblox/nios_modules/nios_txt_record_module.html
fetched_at: 2026-07-28T02:36:08+00:00
---
# infoblox.nios_modules.nios_txt_record module – Configure Infoblox NIOS txt records

> **Note:**
>
> This module is part of the [infoblox.nios_modules collection](https://galaxy.ansible.com/ui/repo/published/infoblox/nios_modules/) (version 1.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infoblox.nios_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](nios_txt_record_module.md#ansible-collections-infoblox-nios-modules-nios-txt-record-module-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_txt_record`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_txt_record_module.md#synopsis)
- [Requirements](nios_txt_record_module.md#requirements)
- [Parameters](nios_txt_record_module.md#parameters)
- [Notes](nios_txt_record_module.md#notes)
- [Examples](nios_txt_record_module.md#examples)

## [Synopsis](nios_txt_record_module.md#id1)

- Adds and/or removes instances of txt record objects from Infoblox NIOS servers. This module manages NIOS `record:txt` objects using the Infoblox WAPI interface over REST.

## [Requirements](nios_txt_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- infoblox_client

## [Parameters](nios_txt_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Configures a text string comment to be associated with the instance of this object. The provided text string will be configured on the object instance. |
| **extattrs**  dictionary | Allows for the configuration of Extensible Attributes on the instance of the object. This argument accepts a set of key / value pairs for configuration. |
| **name**  string / required | Specifies the fully qualified hostname to add or remove from the system. Users can also update the name as it is possible to pass a dict containing *new_name*, *old_name*. See examples. |
| **provider**  dictionary | A dict object containing connection details. |
| **cert**  string | Specifies the client certificate file with digest of x509 config for extra layer secure connection the remote instance of NIOS.  Value can also be specified using `INFOBLOX_CERT` environment variable. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST  Value can also be specified using `INFOBLOX_HOST` environment variable. |
| **http_pool_connections**  integer | Insert decription here  **Default:** `10` |
| **http_pool_maxsize**  integer | Insert description here  **Default:** `10` |
| **http_request_timeout**  integer | The amount of time before to wait before receiving a response  Value can also be specified using `INFOBLOX_HTTP_REQUEST_TIMEOUT` environment variable.  **Default:** `10` |
| **key**  string | Specifies private key file for encryption with the certificate in order to connect with remote instance of NIOS.  Value can also be specified using `INFOBLOX_KEY` environment variable. |
| **max_results**  integer | Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.  Value can also be specified using `INFOBLOX_MAX_RESULTS` environment variable.  **Default:** `1000` |
| **max_retries**  integer | Configures the number of attempted retries before the connection is declared usable  Value can also be specified using `INFOBLOX_MAX_RETRIES` environment variable.  **Default:** `3` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_PASSWORD` environment variable. |
| **silent_ssl_warnings**  boolean | Insert description here  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_USERNAME` environment variable. |
| **validate_certs**  aliases: ssl_verify  boolean | Boolean value to enable or disable verifying SSL certificates  Value can also be specified using `INFOBLOX_SSL_VERIFY` environment variable.  **Choices:**   - `false` ← (default) - `true` |
| **wapi_version**  string | Specifies the version of WAPI to use  Value can also be specified using `INFOBLOX_WAP_VERSION` environment variable.  Until ansible 2.8 the default WAPI was 1.4  **Default:** `"2.9"` |
| **state**  string | Configures the intended state of the instance of the object on the NIOS server. When this value is set to `present`, the object is configured on the device and when this value is set to `absent` the value is removed (if necessary) from the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **text**  string / required | Text associated with the record. It can contain up to 255 bytes per substring, up to a total of 512 bytes. To enter leading, trailing, or embedded spaces in the text, add quotes around the text to preserve the spaces. |
| **ttl**  integer | Configures the TTL to be associated with this txt record. |
| **view**  aliases: dns_view  string | Sets the DNS view to associate this tst record with. The DNS view must already be configured on the system.  **Default:** `"default"` |

## [Notes](nios_txt_record_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - This module must be run locally, which can be achieved by specifying `connection: local`.
> - Please read the :ref:`nios_guide` for more detailed information on how to use Infoblox with Ansible.

## [Examples](nios_txt_record_module.md#id5)

```yaml+jinja
- name: Ensure a text Record Exists
  infoblox.nios_modules.nios_txt_record:
    name: fqdn.txt.record.com
    text: mytext
    state: present
    view: External
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin

- name: Update name of TXT record
  infoblox.nios_modules.nios_txt_record:
    name: {old_name: sample.txtrecord.com, new_name: newsample.txtrecord.com}
    text: mytext
    state: present
    view: External
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Ensure a text Record does not exist
  infoblox.nios_modules.nios_txt_record:
    name: fqdn.txt.record.com
    text: mytext
    state: absent
    view: External
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
```

### Authors

- Corey Wanless (@coreywan)

### Collection links

- [Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
- [Homepage](https://github.com/infobloxopen/infoblox-ansible)
- [Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
