---
collection: ansible
version: "8"
title: "community.network.bigmon_chain module – Create and remove a bigmon inline service chain."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/bigmon_chain_module.html
fetched_at: 2026-07-28T01:55:08+00:00
---
# community.network.bigmon_chain module – Create and remove a bigmon inline service chain.

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
> To use it in a playbook, specify: `community.network.bigmon_chain`.

- [Synopsis](bigmon_chain_module.md#synopsis)
- [Parameters](bigmon_chain_module.md#parameters)
- [Examples](bigmon_chain_module.md#examples)

## [Synopsis](bigmon_chain_module.md#id1)

- Create and remove a bigmon inline service chain.

Aliases: network.bigswitch.bigmon_chain

## [Parameters](bigmon_chain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Bigmon access token. If this isn’t set, the environment variable `BIGSWITCH_ACCESS_TOKEN` is used. |
| **controller**  string / required | The controller IP address. |
| **name**  string / required | The name of the chain. |
| **state**  string | Whether the service chain should be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](bigmon_chain_module.md#id3)

```yaml+jinja
- name: Bigmon inline service chain
  community.network.bigmon_chain:
    name: MyChain
    controller: '{{ inventory_hostname }}'
    state: present
    validate_certs: false
```

### Authors

- Ted (@tedelhourani)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
