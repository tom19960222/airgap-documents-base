---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_server module – Create and manage cloud servers on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_server_module.html
fetched_at: 2026-07-28T02:34:10+00:00
---
# hetzner.hcloud.hcloud_server module – Create and manage cloud servers on the Hetzner Cloud.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/ui/repo/published/hetzner/hcloud/) (version 1.16.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_server_module.md#ansible-collections-hetzner-hcloud-hcloud-server-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_server`.

- [Synopsis](hcloud_server_module.md#synopsis)
- [Requirements](hcloud_server_module.md#requirements)
- [Parameters](hcloud_server_module.md#parameters)
- [See Also](hcloud_server_module.md#see-also)
- [Examples](hcloud_server_module.md#examples)
- [Return Values](hcloud_server_module.md#return-values)

## [Synopsis](hcloud_server_module.md#id1)

- Create, update and manage cloud servers on the Hetzner Cloud.

## [Requirements](hcloud_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_deprecated_image**  boolean | Allows the creation of servers with deprecated images.  **Choices:**   - `false` ← (default) - `true` |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **backups**  boolean | Enable or disable Backups for the given Server.  **Choices:**   - `false` - `true` |
| **datacenter**  string | Datacenter of Server.  Required of no *location* is given and server does not exist. |
| **delete_protection**  boolean | Protect the Server for deletion.  Needs to be the same as *rebuild_protection*.  **Choices:**   - `false` - `true` |
| **enable_ipv4**  boolean | Enables the public ipv4 address  **Choices:**   - `false` - `true` ← (default) |
| **enable_ipv6**  boolean | Enables the public ipv6 address  **Choices:**   - `false` - `true` ← (default) |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **firewalls**  list / elements=string | List of Firewall IDs that should be attached to the server on server creation. |
| **force**  boolean | Force the update of the server.  May power off the server if update.  **Choices:**   - `false` ← (default) - `true` |
| **force_upgrade**  boolean | Deprecated  Force the upgrade of the server.  Power off the server if it is running on upgrade.  **Choices:**   - `false` - `true` |
| **id**  integer | The ID of the Hetzner Cloud server to manage.  Only required if no server *name* is given |
| **image**  string | Image the server should be created from.  Required if server does not exist. |
| **ipv4**  string | ID of the ipv4 Primary IP to use. If omitted and enable_ipv4 is true, a new ipv4 Primary IP will automatically be created |
| **ipv6**  string | ID of the ipv6 Primary IP to use. If omitted and enable_ipv6 is true, a new ipv6 Primary IP will automatically be created. |
| **labels**  dictionary | User-defined labels (key-value pairs). |
| **location**  string | Location of Server.  Required if no *datacenter* is given and server does not exist. |
| **name**  string | The Name of the Hetzner Cloud server to manage.  Only required if no server *id* is given or a server does not exist. |
| **placement_group**  string | Placement Group of the server. |
| **private_networks**  list / elements=string | List of private networks the server is attached to (name or ID)  If None, private networks are left as they are (e.g. if previously added by hcloud_server_network), if it has any other value (including []), only those networks are attached to the server. |
| **rebuild_protection**  boolean | Protect the Server for rebuild.  Needs to be the same as *delete_protection*.  **Choices:**   - `false` - `true` |
| **rescue_mode**  string | Add the Hetzner rescue system type you want the server to be booted into. |
| **server_type**  string | The Server Type of the Hetzner Cloud server to manage.  Required if server does not exist. |
| **ssh_keys**  list / elements=string | List of SSH key names  The key names correspond to the SSH keys configured for your Hetzner Cloud account access. |
| **state**  string | State of the server.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"restarted"` - `"started"` - `"stopped"` - `"rebuild"` |
| **upgrade_disk**  boolean | Resize the disk size, when resizing a server.  If you want to downgrade the server later, this value should be False.  **Choices:**   - `false` ← (default) - `true` |
| **user_data**  string | User Data to be passed to the server on creation.  Only used if server does not exist. |
| **volumes**  list / elements=string | List of Volumes IDs that should be attached to the server on server creation. |

## [See Also](hcloud_server_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_server_module.md#id5)

```yaml+jinja
- name: Create a basic server
  hcloud_server:
    name: my-server
    server_type: cx11
    image: ubuntu-22.04
    state: present

- name: Create a basic server with ssh key
  hcloud_server:
    name: my-server
    server_type: cx11
    image: ubuntu-22.04
    location: fsn1
    ssh_keys:
      - me@myorganisation
    state: present

- name: Resize an existing server
  hcloud_server:
    name: my-server
    server_type: cx21
    upgrade_disk: true
    state: present

- name: Ensure the server is absent (remove if needed)
  hcloud_server:
    name: my-server
    state: absent

- name: Ensure the server is started
  hcloud_server:
    name: my-server
    state: started

- name: Ensure the server is stopped
  hcloud_server:
    name: my-server
    state: stopped

- name: Ensure the server is restarted
  hcloud_server:
    name: my-server
    state: restarted

- name: Ensure the server is will be booted in rescue mode and therefore restarted
  hcloud_server:
    name: my-server
    rescue_mode: linux64
    state: restarted

- name: Ensure the server is rebuild
  hcloud_server:
    name: my-server
    image: ubuntu-22.04
    state: rebuild

- name: Add server to placement group
  hcloud_server:
    name: my-server
    placement_group: my-placement-group
    force: True
    state: present

- name: Remove server from placement group
  hcloud_server:
    name: my-server
    placement_group: null
    state: present

- name: Add server with private network only
  hcloud_server:
    name: my-server
    enable_ipv4: false
    enable_ipv6: false
    private_networks:
      - my-network
      - 4711
    state: present
```

## [Return Values](hcloud_server_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_server**  complex | The server instance  **Returned:** Always |
| **backup_window**  boolean | Time window (UTC) in which the backup will run, or null if the backups are not enabled  **Returned:** always  **Sample:** `"22-02"` |
| **datacenter**  string | Name of the datacenter of the server  **Returned:** always  **Sample:** `"fsn1-dc14"` |
| **delete_protection**  boolean  *added in hetzner.hcloud 0.1.0* | True if server is protected for deletion  **Returned:** always  **Sample:** `false` |
| **id**  integer | Numeric identifier of the server  **Returned:** always  **Sample:** `1937415` |
| **ipv4_address**  string | Public IPv4 address of the server  **Returned:** always  **Sample:** `"116.203.104.109"` |
| **ipv6**  string | IPv6 network of the server  **Returned:** always  **Sample:** `"2a01:4f8:1c1c:c140::/64"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** always |
| **location**  string | Name of the location of the server  **Returned:** always  **Sample:** `"fsn1"` |
| **name**  string | Name of the server  **Returned:** always  **Sample:** `"my-server"` |
| **placement_group**  string  *added in hetzner.hcloud 1.5.0* | Placement Group of the server  **Returned:** always  **Sample:** `"4711"` |
| **private_networks**  list / elements=string | List of private networks the server is attached to (name or ID)  **Returned:** always  **Sample:** `["my-network", "another-network", "4711"]` |
| **private_networks_info**  list / elements=dictionary | List of private networks the server is attached to (dict with name and ip)  **Returned:** always  **Sample:** `[{"ip": "192.168.1.1", "name": "my-network"}, {"ip": "10.185.50.40", "name": "another-network"}]` |
| **rebuild_protection**  boolean  *added in hetzner.hcloud 0.1.0* | True if server is protected for rebuild  **Returned:** always  **Sample:** `false` |
| **rescue_enabled**  boolean | True if rescue mode is enabled, Server will then boot into rescue system on next reboot  **Returned:** always  **Sample:** `false` |
| **server_type**  string | Name of the server type of the server  **Returned:** always  **Sample:** `"cx11"` |
| **status**  string | Status of the server  **Returned:** always  **Sample:** `"running"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
