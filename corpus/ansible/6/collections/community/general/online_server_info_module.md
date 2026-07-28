---
collection: ansible
version: "6"
title: "community.general.online_server_info module – Gather information about Online servers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/online_server_info_module.html
fetched_at: 2026-07-27T17:11:32+00:00
---
# community.general.online_server_info module – Gather information about Online servers

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.online_server_info`.

- [Synopsis](online_server_info_module.md#synopsis)
- [Parameters](online_server_info_module.md#parameters)
- [Notes](online_server_info_module.md#notes)
- [Examples](online_server_info_module.md#examples)
- [Return Values](online_server_info_module.md#return-values)

## [Synopsis](online_server_info_module.md#id1)

- Gather information about the servers.
- <https://www.online.net/en/dedicated-server>

## [Parameters](online_server_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Online API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Online OAuth token. |
| **api_url**  aliases: base_url  string | Online API URL  Default: `"https://api.online.net"` |
| **validate_certs**  boolean | Validate SSL certs of the Online API.  Choices:   - `false` - `true` ← (default) |

## [Notes](online_server_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://console.online.net/en/api/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `ONLINE_TOKEN`, `ONLINE_API_KEY`, `ONLINE_OAUTH_TOKEN`, `ONLINE_API_TOKEN`
> - If one wants to use a different `api_url` one can also set the `ONLINE_API_URL` environment variable.

## [Examples](online_server_info_module.md#id4)

```yaml+jinja
- name: Gather Online server information
  community.general.online_server_info:
    api_token: '0d1627e8-bbf0-44c5-a46f-5c4d3aef033f'
  register: result

- ansible.builtin.debug:
    msg: "{{ result.online_server_info }}"
```

## [Return Values](online_server_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **online_server_info**  list / elements=dictionary | Response from Online API.  For more details please refer to: <https://console.online.net/en/api/>.  Returned: success  Sample: `{"online_server_info": [{"abuse": "abuse@example.com", "anti_ddos": false, "bmc": {"session_key": null}, "boot_mode": "normal", "contacts": {"owner": "foobar", "tech": "foobar"}, "disks": [{"$ref": "/api/v1/server/hardware/disk/68452"}, {"$ref": "/api/v1/server/hardware/disk/68453"}], "drive_arrays": [{"disks": [{"$ref": "/api/v1/server/hardware/disk/68452"}, {"$ref": "/api/v1/server/hardware/disk/68453"}], "raid_controller": {"$ref": "/api/v1/server/hardware/raidController/9910"}, "raid_level": "RAID1"}], "hardware_watch": true, "hostname": "sd-42", "id": 42, "ip": [{"address": "195.154.172.149", "mac": "28:92:4a:33:5e:c6", "reverse": "195-154-172-149.rev.poneytelecom.eu.", "switch_port_state": "up", "type": "public"}, {"address": "10.90.53.212", "mac": "28:92:4a:33:5e:c7", "reverse": null, "switch_port_state": "up", "type": "private"}], "last_reboot": "2018-08-23T08:32:03.000Z", "location": {"block": "A", "datacenter": "DC3", "position": 19, "rack": "A23", "room": "4 4-4"}, "network": {"ip": ["195.154.172.149"], "ipfo": [], "private": ["10.90.53.212"]}, "offer": "Pro-1-S-SATA", "os": {"name": "FreeBSD", "version": "11.1-RELEASE"}, "power": "ON", "proactive_monitoring": false, "raid_controllers": [{"$ref": "/api/v1/server/hardware/raidController/9910"}], "support": "Basic service level"}]}` |

### Authors

- Remy Leone (@remyleone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
