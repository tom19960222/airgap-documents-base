---
collection: ansible
version: "8"
title: "community.network.iap_token module – Get token for the Itential Automation Platform"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/iap_token_module.html
fetched_at: 2026-07-28T01:56:44+00:00
---
# community.network.iap_token module – Get token for the Itential Automation Platform

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.iap_token`.

- [Synopsis](iap_token_module.md#synopsis)
- [Parameters](iap_token_module.md#parameters)
- [Examples](iap_token_module.md#examples)
- [Return Values](iap_token_module.md#return-values)

## [Synopsis](iap_token_module.md#id1)

- Checks the connection to IAP and retrieves a login token.

Aliases: network.itential.iap_token

## [Parameters](iap_token_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **https**  boolean | Use HTTPS to connect  By default using http  **Choices:**   - `false` ← (default) - `true` |
| **iap_fqdn**  string / required | Provide the fqdn or ip-address for the Itential Automation Platform |
| **iap_port**  string / required | Provide the port number for the Itential Automation Platform |
| **password**  string / required | Provide the password for the Itential Automation Platform |
| **username**  string / required | Provide the username for the Itential Automation Platform |
| **validate_certs**  boolean | If `no`, SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](iap_token_module.md#id3)

```yaml+jinja
- name: Get token for the Itential Automation Platform
  community.network.iap_token:
    iap_port: 3000
    iap_fqdn: localhost
    username: myusername
    password: mypass
  register: result

- ansible.builtin.debug: var=result.token
```

## [Return Values](iap_token_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **token**  string | The token acquired from the Itential Automation Platform  **Returned:** always |

### Authors

- Itential (@cma0)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
