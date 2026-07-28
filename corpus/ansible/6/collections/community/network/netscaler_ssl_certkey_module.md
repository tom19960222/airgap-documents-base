---
collection: ansible
version: "6"
title: "community.network.netscaler_ssl_certkey module – Manage ssl certificate keys."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/netscaler_ssl_certkey_module.html
fetched_at: 2026-07-27T17:19:08+00:00
---
# community.network.netscaler_ssl_certkey module – Manage ssl certificate keys.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](netscaler_ssl_certkey_module.md#ansible-collections-community-network-netscaler-ssl-certkey-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_ssl_certkey`.

- [Synopsis](netscaler_ssl_certkey_module.md#synopsis)
- [Requirements](netscaler_ssl_certkey_module.md#requirements)
- [Parameters](netscaler_ssl_certkey_module.md#parameters)
- [Notes](netscaler_ssl_certkey_module.md#notes)
- [Examples](netscaler_ssl_certkey_module.md#examples)
- [Return Values](netscaler_ssl_certkey_module.md#return-values)

## [Synopsis](netscaler_ssl_certkey_module.md#id1)

- Manage ssl certificate keys.

## [Requirements](netscaler_ssl_certkey_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_ssl_certkey_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  string | Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. The certificate file should be present on the appliance’s hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.  Minimum length = 1 |
| **certkey**  string | Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore `_` character, and must contain only ASCII alphanumeric, underscore `_`, hash `#`, period `.`, space , colon `:`, at `@`, equals `=`, and hyphen `-` characters. Cannot be changed after the certificate-key pair is created.  The following requirement applies only to the NetScaler CLI:  If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, “my cert” or ‘my cert’).  Minimum length = 1 |
| **expirymonitor**  string | Issue an alert when the certificate is about to expire.  Choices:   - `"enabled"` - `"disabled"` |
| **inform**  string | Input format of the certificate and the private-key files. The three formats supported by the appliance are:  PEM - Privacy Enhanced Mail  DER - Distinguished Encoding Rule  PFX - Personal Information Exchange.  Choices:   - `"DER"` - `"PEM"` - `"PFX"` |
| **key**  string | Name of and, optionally, path to the private-key file that is used to form the certificate-key pair. The certificate file should be present on the appliance’s hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.  Minimum length = 1 |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  Choices:   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  Default: `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **notificationperiod**  string | Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire.  Minimum value = `10`  Maximum value = `100` |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **passplain**  string | Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM format.  Minimum length = 1 |
| **password**  string | Passphrase that was used to encrypt the private-key. Use this option to load encrypted private-keys in PEM format. |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  Choices:   - `false` - `true` ← (default) |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  Choices:   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](netscaler_ssl_certkey_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_ssl_certkey_module.md#id5)

```yaml+jinja
- name: Setup ssl certkey
  delegate_to: localhost
  community.network.netscaler_ssl_certkey:
    nitro_user: nsroot
    nitro_pass: nsroot
    nsip: 172.18.0.2

    certkey: certirificate_1
    cert: server.crt
    key: server.key
    expirymonitor: enabled
    notificationperiod: 30
    inform: PEM
    password: False
    passplain: somesecret
```

## [Return Values](netscaler_ssl_certkey_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  dictionary | List of differences between the actual configured object and the configuration specified in the module  Returned: failure  Sample: `{"targetlbvserver": "difference. ours: (str) server1 other: (str) server2"}` |
| **loglines**  list / elements=string | list of logged messages by the module  Returned: always  Sample: `["['message 1'", " 'message 2']"]` |
| **msg**  string | Message detailing the failure reason  Returned: failure  Sample: `"Action does not exist"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
