---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_sshkeypair module – Manages SSH keys on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_sshkeypair_module.html
fetched_at: 2026-07-28T00:15:48+00:00
---
# ngine_io.cloudstack.cs_sshkeypair module – Manages SSH keys on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_sshkeypair_module.md#ansible-collections-ngine-io-cloudstack-cs-sshkeypair-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_sshkeypair`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_sshkeypair_module.md#synopsis)
- [Requirements](cs_sshkeypair_module.md#requirements)
- [Parameters](cs_sshkeypair_module.md#parameters)
- [Notes](cs_sshkeypair_module.md#notes)
- [Examples](cs_sshkeypair_module.md#examples)
- [Return Values](cs_sshkeypair_module.md#return-values)

## [Synopsis](cs_sshkeypair_module.md#id1)

- Create, register and remove SSH keys.
- If no key was found and no public key was provided and a new SSH private/public key pair will be created and the private key will be returned.

## [Requirements](cs_sshkeypair_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_sshkeypair_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the public key is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the public key is related to. |
| **name**  string / required | Name of public key. |
| **project**  string | Name of the project the public key to be registered in. |
| **public_key**  string | String of the public key. |
| **state**  string | State of the public key.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](cs_sshkeypair_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_sshkeypair_module.md#id5)

```yaml+jinja
- name: create a new private / public key pair
  ngine_io.cloudstack.cs_sshkeypair:
    name: linus@example.com
  register: key

- debug:
    msg: 'Private key is {{ key.private_key }}'

- name: remove a public key by its name
  ngine_io.cloudstack.cs_sshkeypair:
    name: linus@example.com
    state: absent

- name: register your existing local public key
  ngine_io.cloudstack.cs_sshkeypair:
    name: linus@example.com
    public_key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
```

## [Return Values](cs_sshkeypair_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **fingerprint**  string | Fingerprint of the SSH public key.  Returned: success  Sample: `"86:5e:a3:e8:bd:95:7b:07:7c:c2:5c:f7:ad:8b:09:28"` |
| **id**  string | UUID of the SSH public key.  Returned: success  Sample: `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **name**  string | Name of the SSH public key.  Returned: success  Sample: `"linus@example.com"` |
| **private_key**  string | Private key of generated SSH keypair.  Returned: changed  Sample: `"-----BEGIN RSA PRIVATE KEY----- MII...8tO -----END RSA PRIVATE KEY----- "` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
