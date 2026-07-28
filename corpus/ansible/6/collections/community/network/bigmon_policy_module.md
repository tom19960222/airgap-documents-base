---
collection: ansible
version: "6"
title: "community.network.bigmon_policy module – Create and remove a bigmon out-of-band policy."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/bigmon_policy_module.html
fetched_at: 2026-07-27T17:17:11+00:00
---
# community.network.bigmon_policy module – Create and remove a bigmon out-of-band policy.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.bigmon_policy`.

- [Synopsis](bigmon_policy_module.md#synopsis)
- [Parameters](bigmon_policy_module.md#parameters)
- [Examples](bigmon_policy_module.md#examples)

## [Synopsis](bigmon_policy_module.md#id1)

- Create and remove a bigmon out-of-band policy.

## [Parameters](bigmon_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Bigmon access token. If this isn’t set, the environment variable `BIGSWITCH_ACCESS_TOKEN` is used. |
| **action**  string | Forward matching packets to delivery interfaces, Drop is for measure rate of matching packets, but do not forward to delivery interfaces, capture packets and write to a PCAP file, or enable NetFlow generation.  Choices:   - `"forward"` ← (default) - `"drop"` - `"flow-gen"` |
| **controller**  string / required | The controller address. |
| **delivery_packet_count**  string | Run policy until delivery_packet_count packets are delivered.  Default: `0` |
| **duration**  string | Run policy for duration duration or until delivery_packet_count packets are delivered, whichever comes first.  Default: `0` |
| **name**  string / required | The name of the policy. |
| **policy_description**  string | Description of policy. |
| **priority**  string | A priority associated with this policy. The higher priority policy takes precedence over a lower priority.  Default: `100` |
| **start_time**  string | Date the policy becomes active  Default: `"ansible_date_time.iso8601"` |
| **state**  string | Whether the policy should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](bigmon_policy_module.md#id3)

```yaml+jinja
- name: Policy to aggregate filter and deliver data center (DC) 1 traffic
  community.network.bigmon_policy:
    name: policy1
    policy_description: DC 1 traffic policy
    action: drop
    controller: '{{ inventory_hostname }}'
    state: present
    validate_certs: false
```

### Authors

- Ted (@tedelhourani)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
