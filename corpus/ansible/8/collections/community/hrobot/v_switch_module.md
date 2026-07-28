---
collection: ansible
version: "8"
title: "community.hrobot.v_switch module – Manage Hetzner’s vSwitch"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/hrobot/v_switch_module.html
fetched_at: 2026-07-28T01:53:49+00:00
---
# community.hrobot.v_switch module – Manage Hetzner’s vSwitch

> **Note:**
>
> This module is part of the [community.hrobot collection](https://galaxy.ansible.com/ui/repo/published/community/hrobot/) (version 1.8.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hrobot`.
>
> To use it in a playbook, specify: `community.hrobot.v_switch`.

New in community.hrobot 1.7.0

- [Synopsis](v_switch_module.md#synopsis)
- [Parameters](v_switch_module.md#parameters)
- [Attributes](v_switch_module.md#attributes)
- [See Also](v_switch_module.md#see-also)
- [Examples](v_switch_module.md#examples)
- [Return Values](v_switch_module.md#return-values)

## [Synopsis](v_switch_module.md#id1)

- Manage Hetzner’s vSwitch.

## [Parameters](v_switch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **name**  string / required | The vSwitch’s name.  In order to identify a vSwitch both name and VLAN must match. If not, a new vSwitch will be created. |
| **servers**  list / elements=string | List of server identifiers (server’s numeric ID or server’s main IPv4 or IPv6).  If servers is not specified, servers are not going to be deleted. |
| **state**  string | State of the vSwitch.  vSwitch is created if state is `present`, and deleted if state is `absent`.  `absent` just cancels the vSwitch at the end of the current day.  When cancelling, you have to specify `servers=[]` if you want to actively remove the servers in the vSwitch.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Timeout (in seconds) for waiting for vSwitch servers to be configured.  **Default:** `180` |
| **vlan**  integer / required | The vSwitch’s VLAN ID.  Range can be from 4000 to 4091.  In order to identify a vSwitch both name and VLAN must match. If not, a new vSwitch will be created. |
| **wait**  boolean | Whether to wait until the vSwitch has been successfully configured before determining what to do, and before returning from the module.  The API returns status `in process` when the vSwitch is currently being set up in the servers. If this happens, the module will try again until the status changes to `ready` or server has been removed from vSwitch.  Please note that if you disable wait while deleting and removing servers module will fail with `VSWITCH_IN_PROCESS` error.  **Choices:**   - `false` - `true` ← (default) |
| **wait_delay**  integer | Delay to wait (in seconds) before checking again whether the vSwitch servers has been configured.  **Default:** `10` |

## [Attributes](v_switch_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.hrobot.robot** | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](v_switch_module.md#id4)

> **See also:**
>
> [vSwitch documentation](https://docs.hetzner.com/robot/dedicated-server/network/vswitch)
> :   Hetzner’s documentation on vSwitch for connecting dedicated servers.

## [Examples](v_switch_module.md#id5)

```yaml+jinja
- name: Create vSwitch with VLAN 4010 and name foo
  community.hrobot.v_switch:
    hetzner_user: foo
    hetzner_password: bar
    vlan: 4010
    name: foo

- name: Create vSwitch with VLAN 4020 and name foo with two servers
  community.hrobot.v_switch:
    hetzner_user: foo
    hetzner_password: bar
    vlan: 4010
    name: foo
    servers:
      - 123.123.123.123
      - 154323
```

## [Return Values](v_switch_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **v_switch**  dictionary | Information on the vSwitch.  **Returned:** success |
| **cancelled**  boolean | Cancellation status.  **Returned:** success  **Sample:** `false` |
| **cloud_network**  list / elements=dictionary | List of assigned Cloud networks.  **Returned:** success  **Sample:** `[{"gateway": "10.0.2.1", "id": 123, "ip": "10.0.2.0", "mask": 24}]` |
| **gateway**  string | Gateway.  **Returned:** success  **Sample:** `"10.0.2.1"` |
| **id**  integer | Cloud network ID.  **Returned:** success  **Sample:** `123` |
| **ip**  string | IP address.  **Returned:** success  **Sample:** `"10.0.2.0"` |
| **mask**  integer | Subnet mask in CIDR notation.  **Returned:** success  **Sample:** `24` |
| **id**  integer | The vSwitch’s ID.  **Returned:** success  **Sample:** `4321` |
| **name**  string | The vSwitch’s name.  **Returned:** success  **Sample:** `"my vSwitch"` |
| **server**  list / elements=dictionary | The vSwitch’s VLAN.  **Returned:** success  **Sample:** `[{"server_ip": "123.123.123.123", "server_ipv6_net": "2a01:4f8:111:4221::", "server_number": 321, "status": "ready"}]` |
| **server_ip**  string | The server’s main IP address.  **Returned:** success  **Sample:** `"123.123.123.123"` |
| **server_ipv6_net**  string | The server’s main IPv6 network address.  **Returned:** success  **Sample:** `"2a01:f48:111:4221::"` |
| **server_number**  integer | The server’s numeric ID.  **Returned:** success  **Sample:** `321` |
| **status**  string | Status of vSwitch for this server.  **Returned:** success  **Can only return:**   - `"ready"` - `"in process"` - `"failed"`   **Sample:** `"ready"` |
| **subnet**  list / elements=dictionary | List of assigned IP addresses.  **Returned:** success  **Sample:** `[{"gateway": "213.239.252.49", "ip": "213.239.252.48", "mask": 29}]` |
| **gateway**  string | Gateway of the subnet.  **Returned:** success  **Sample:** `"213.239.252.49"` |
| **ip**  string | IP address.  **Returned:** success  **Sample:** `"213.239.252.48"` |
| **mask**  integer | Subnet mask in CIDR notation.  **Returned:** success  **Sample:** `29` |
| **vlan**  integer | The vSwitch’s VLAN ID.  **Returned:** success  **Sample:** `4000` |

### Authors

- Alexander Gil Casas (@pando85)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
- [Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-hrobot)
