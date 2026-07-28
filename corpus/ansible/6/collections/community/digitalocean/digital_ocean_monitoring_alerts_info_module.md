---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_monitoring_alerts_info module – Programmatically retrieve metrics as well as configure alert policies based on these metrics"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_monitoring_alerts_info_module.html
fetched_at: 2026-07-27T17:06:50+00:00
---
# community.digitalocean.digital_ocean_monitoring_alerts_info module – Programmatically retrieve metrics as well as configure alert policies based on these metrics

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_monitoring_alerts_info`.

New in community.digitalocean 1.10.0

- [Synopsis](digital_ocean_monitoring_alerts_info_module.md#synopsis)
- [Parameters](digital_ocean_monitoring_alerts_info_module.md#parameters)
- [Examples](digital_ocean_monitoring_alerts_info_module.md#examples)
- [Return Values](digital_ocean_monitoring_alerts_info_module.md#return-values)

## [Synopsis](digital_ocean_monitoring_alerts_info_module.md#id1)

- The DigitalOcean Monitoring API makes it possible to programmatically retrieve metrics as well as configure alert policies based on these metrics.
- The Monitoring API can help you gain insight into how your apps are performing and consuming resources.

## [Parameters](digital_ocean_monitoring_alerts_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **oauth_token**  aliases: API_TOKEN  string / required | DigitalOcean OAuth token; can be specified in `DO_API_KEY`, `DO_API_TOKEN`, or `DO_OAUTH_TOKEN` environment variables |
| **state**  string | `present` to return alerts  Choices:   - `"present"` ← (default) |
| **uuid**  string | Alert uuid (if specified only returns the specific alert policy) |

## [Examples](digital_ocean_monitoring_alerts_info_module.md#id3)

```yaml+jinja
- name: Get Droplet Monitoring alerts polices
  community.digitalocean.digital_ocean_monitoring_alerts_info:
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
  register: monitoring_alerts

- name: Get specific Droplet Monitoring alerts policy
  community.digitalocean.digital_ocean_monitoring_alerts_info:
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    uuid: ec48b0e7-23bb-4a7f-95f2-d83da62fcd60
  register: monitoring_alert
```

## [Return Values](digital_ocean_monitoring_alerts_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | DigitalOcean Monitoring alerts policies  Returned: changed  Sample: `{"data": [{"alerts": {"email": ["mamercad@gmail.com"], "slack": []}, "compare": "GreaterThan", "description": "Droplet load1 alert", "enabled": true, "entities": ["262383737"], "tags": ["my_alert_tag"], "type": "v1/insights/droplet/load_1", "uuid": "ec48b0e7-23bb-4a7f-95f2-d83da62fcd60", "value": 3.14159, "window": "5m"}]}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
