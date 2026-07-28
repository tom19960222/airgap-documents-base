---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_pod module – Manage AC pods in Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_pod_module.html
fetched_at: 2026-07-28T02:51:17+00:00
---
# purestorage.flasharray.purefa_pod module – Manage AC pods in Pure Storage FlashArrays

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_pod_module.md#ansible-collections-purestorage-flasharray-purefa-pod-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_pod`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_pod_module.md#synopsis)
- [Requirements](purefa_pod_module.md#requirements)
- [Parameters](purefa_pod_module.md#parameters)
- [Notes](purefa_pod_module.md#notes)
- [Examples](purefa_pod_module.md#examples)

## [Synopsis](purefa_pod_module.md#id1)

- Manage AC pods in a Pure Storage FlashArray.

## [Requirements](purefa_pod_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_pod_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **eradicate**  boolean | Define whether to eradicate the pod on delete or leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **failover**  list / elements=string | The name of the array given priority to stay online if arrays loose contact with eachother.  Oprions are either array in the cluster, or *auto* |
| **ignore_usage**  boolean  *added in purestorage.flasharray 1.18.0* | Flag used to override checks for quota management operations.  If set to true, pod usage is not checked against the quota_limits that are set.  If set to false, the actual logical bytes in use are prevented from exceeding the limits set on the pod.  Client operations might be impacted.  If the limit exceeds the quota, the operation is not allowed.  **Choices:**   - `false` ← (default) - `true` |
| **mediator**  string | Name of the mediator to use for a pod  **Default:** `"purestorage"` |
| **name**  string / required | The name of the pod. |
| **promote**  boolean | Promote/demote any pod not in a stretched relationship. .  Demoting a pod will render it read-only.  **Choices:**   - `false` - `true` |
| **quiesce**  boolean | Quiesce/Skip quiesce when *promote* is false and demoting an ActiveDR pod.  Quiesce will ensure all local data has been replicated before demotion.  Skipping quiesce looses all pending data to be replicated to the remote pod.  Can only demote the pod if it is in a Acrive DR replica link relationship.  This will default to True  **Choices:**   - `false` - `true` |
| **quota**  string  *added in purestorage.flasharray 1.18.0* | Logical quota limit of the pod in K, M, G, T or P units, or bytes. |
| **state**  string | Define whether the pod should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **stretch**  string | The name of the array to stretch to/unstretch from. Must be synchromously replicated.  To unstretch an array use state *absent*  You can only specify a remote array, ie you cannot unstretch a pod from the current array and then restretch back to the current array.  To restretch a pod you must perform this from the remaining array the pod resides on. |
| **target**  string | Name of clone target pod. |
| **undo**  boolean | Use the *undo-remote* pod when *promote* is true and promoting an ActiveDR pod.  This will default to True  **Choices:**   - `false` - `true` |

## [Notes](purefa_pod_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_pod_module.md#id5)

```yaml+jinja
- name: Create new pod named foo
  purestorage.flasharray.purefa_pod:
    name: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete and eradicate pod named foo
  purestorage.flasharray.purefa_pod:
    name: foo
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Set failover array for pod named foo
  purestorage.flasharray.purefa_pod:
    name: foo
    failover:
    - array1
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set mediator for pod named foo
  purestorage.flasharray.purefa_pod:
    name: foo
    mediator: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Stretch a pod named foo to array2
  purestorage.flasharray.purefa_pod:
    name: foo
    stretch: array2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Unstretch a pod named foo from array2
  purestorage.flasharray.purefa_pod:
    name: foo
    stretch: array2
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create clone of pod foo named bar
  purestorage.flasharray.purefa_pod:
    name: foo
    target: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
