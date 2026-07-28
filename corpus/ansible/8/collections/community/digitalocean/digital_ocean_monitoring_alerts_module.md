---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_monitoring_alerts module – Programmatically retrieve metrics as well as configure alert policies based on these metrics"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_monitoring_alerts_module.html
fetched_at: 2026-07-28T01:43:07+00:00
---
# community.digitalocean.digital_ocean_monitoring_alerts module – Programmatically retrieve metrics as well as configure alert policies based on these metrics

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_monitoring_alerts`.

New in community.digitalocean 1.10.0

- [Synopsis](digital_ocean_monitoring_alerts_module.md#synopsis)
- [Parameters](digital_ocean_monitoring_alerts_module.md#parameters)
- [Examples](digital_ocean_monitoring_alerts_module.md#examples)
- [Return Values](digital_ocean_monitoring_alerts_module.md#return-values)

## [Synopsis](digital_ocean_monitoring_alerts_module.md#id1)

- The DigitalOcean Monitoring API makes it possible to programmatically retrieve metrics as well as configure alert policies based on these metrics.
- The Monitoring API can help you gain insight into how your apps are performing and consuming resources.

## [Parameters](digital_ocean_monitoring_alerts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **alerts**  dictionary | Alert object, required for `state=present`  Supports `email["email1", "email2", ...]` and `slack[{"channel1", "url1"}, {"channel2", "url2"}, ...]` |
| **compare**  string | Alert comparison, required for `state=present`  **Choices:**   - `"GreaterThan"` - `"LessThan"` |
| **description**  string | Alert description, required for `state=present` |
| **enabled**  boolean | Enabled or not, required for `state=present`  **Choices:**   - `false` - `true` |
| **entities**  list / elements=string | Alert entities, required for `state=present` |
| **oauth_token**  aliases: API_TOKEN  string / required | DigitalOcean OAuth token; can be specified in `DO_API_KEY`, `DO_API_TOKEN`, or `DO_OAUTH_TOKEN` environment variables |
| **state**  string | The usual, `present` to create, `absent` to destroy  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Alert tags, required for `state=present` |
| **type**  string | Alert type, required for `state=present`  See <https://docs.digitalocean.com/reference/api/api-reference/#operation/create_alert_policy> for valid types  **Choices:**   - `"v1/insights/droplet/load_1"` - `"v1/insights/droplet/load_5"` - `"v1/insights/droplet/load_15"` - `"v1/insights/droplet/memory_utilization_percent"` - `"v1/insights/droplet/disk_utilization_percent"` - `"v1/insights/droplet/cpu"` - `"v1/insights/droplet/disk_read"` - `"v1/insights/droplet/disk_write"` - `"v1/insights/droplet/public_outbound_bandwidth"` - `"v1/insights/droplet/public_inbound_bandwidth"` - `"v1/insights/droplet/private_outbound_bandwidth"` - `"v1/insights/droplet/private_inbound_bandwidth"` |
| **uuid**  string | Alert uuid, required for `state=absent` |
| **value**  float | Alert threshold, required for `state=present` |
| **window**  string | Alert window, required for `state=present`  **Choices:**   - `"5m"` - `"10m"` - `"30m"` - `"1h"` |

## [Examples](digital_ocean_monitoring_alerts_module.md#id3)

```yaml+jinja
- name: Create Droplet Monitoring alerts policy
  community.digitalocean.digital_ocean_monitoring_alerts:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    alerts:
      email: ["alerts@example.com"]
      slack: []
    compare: GreaterThan
    description: Droplet load1 alert
    enabled: true
    entities: ["{{ droplet_id }}"]
    tags: ["my_alert_tag"]
    type: v1/insights/droplet/load_1
    value: 3.14159
    window: 5m
  register: monitoring_alert_policy

- name: Delete Droplet Monitoring alerts policy
  community.digitalocean.digital_ocean_monitoring_alerts:
    state: absent
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    uuid: "{{ monitoring_alert_policy.data.uuid }}"
```

## [Return Values](digital_ocean_monitoring_alerts_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | A DigitalOcean Monitoring alerts policy  **Returned:** changed  **Sample:** `{"alerts": {"email": ["mamercad@gmail.com"], "slack": []}, "compare": "GreaterThan", "description": "Droplet load1 alert", "enabled": true, "entities": ["262383737"], "tags": ["my_alert_tag"], "type": "v1/insights/droplet/load_1", "uuid": "9f988f00-4690-443d-b638-ed5a99bbad3b", "value": 3.14159, "window": "5m"}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
