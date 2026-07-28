---
collection: ansible
version: "8"
title: "community.general.bigpanda module – Notify BigPanda about deployments"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/bigpanda_module.html
fetched_at: 2026-07-28T01:44:48+00:00
---
# community.general.bigpanda module – Notify BigPanda about deployments

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.bigpanda`.

- [Synopsis](bigpanda_module.md#synopsis)
- [Parameters](bigpanda_module.md#parameters)
- [Attributes](bigpanda_module.md#attributes)
- [Examples](bigpanda_module.md#examples)

## [Synopsis](bigpanda_module.md#id1)

- Notify BigPanda when deployments start and end (successfully or not). Returns a deployment object containing all the parameters for future module calls.

Aliases: monitoring.bigpanda

## [Parameters](bigpanda_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **component**  aliases: name  string / required | The name of the component being deployed. Ex: billing |
| **deployment_message**  string  *added in community.general 0.2.0* | Message about the deployment. |
| **description**  string | Free text description of the deployment. |
| **env**  string | The environment name, typically ‘production’, ‘staging’, etc. |
| **hosts**  aliases: host  string | Name of affected host name. Can be a list.  If not specified, it defaults to the remote system’s hostname. |
| **owner**  string | The person responsible for the deployment. |
| **source_system**  string | Source system used in the requests to the API  **Default:** `"ansible"` |
| **state**  string / required | State of the deployment.  **Choices:**   - `"started"` - `"finished"` - `"failed"` |
| **token**  string / required | API token. |
| **url**  string | Base URL of the API server.  **Default:** `"https://api.bigpanda.io"` |
| **validate_certs**  boolean | If `false`, SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **version**  string / required | The deployment version. |

## [Attributes](bigpanda_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](bigpanda_module.md#id4)

```yaml+jinja
- name: Notify BigPanda about a deployment
  community.general.bigpanda:
    component: myapp
    version: '1.3'
    token: '{{ bigpanda_token }}'
    state: started

- name: Notify BigPanda about a deployment
  community.general.bigpanda:
    component: myapp
    version: '1.3'
    token: '{{ bigpanda_token }}'
    state: finished

# If outside servers aren't reachable from your machine, use delegate_to and override hosts:
- name: Notify BigPanda about a deployment
  community.general.bigpanda:
    component: myapp
    version: '1.3'
    token: '{{ bigpanda_token }}'
    hosts: '{{ ansible_hostname }}'
    state: started
  delegate_to: localhost
  register: deployment

- name: Notify BigPanda about a deployment
  community.general.bigpanda:
    component: '{{ deployment.component }}'
    version: '{{ deployment.version }}'
    token: '{{ deployment.token }}'
    state: finished
  delegate_to: localhost
```

### Authors

- Hagai Kariti (@hkariti)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
