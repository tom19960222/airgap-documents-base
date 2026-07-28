---
collection: ansible
version: "6"
title: "Meraki Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_meraki.html
fetched_at: 2026-07-27T16:41:12+00:00
---
# Meraki Platform Options

The [cisco.meraki](https://galaxy.ansible.com/cisco/meraki) collection only supports the `local` connection type at this time.

- [Connections available](platform_meraki.md#connections-available)

  - [Example Meraki task](platform_meraki.md#example-meraki-task)

## [Connections available](platform_meraki.md#id2)

|  | Dashboard API |
| --- | --- |
| Protocol | HTTP(S) |
| Credentials | uses API key from Dashboard |
| Connection Settings | `ansible_connection: localhost` |
| Returned Data Format | `data.` |

### [Example Meraki task](platform_meraki.md#id3)

```yaml
cisco.meraki.meraki_organization:
  auth_key: abc12345
  org_name: YourOrg
  state: present
delegate_to: localhost
```

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
