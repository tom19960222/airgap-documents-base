---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.server module – Manages servers on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/server_module.html
fetched_at: 2026-07-28T01:39:58+00:00
---
# cloudscale_ch.cloud.server module – Manages servers on the cloudscale.ch IaaS service

> **Note:**
>
> This module is part of the [cloudscale_ch.cloud collection](https://galaxy.ansible.com/ui/repo/published/cloudscale_ch/cloud/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloudscale_ch.cloud`.
>
> To use it in a playbook, specify: `cloudscale_ch.cloud.server`.

New in cloudscale_ch.cloud 1.0.0

- [Synopsis](server_module.md#synopsis)
- [Parameters](server_module.md#parameters)
- [Notes](server_module.md#notes)
- [Examples](server_module.md#examples)
- [Return Values](server_module.md#return-values)

## [Synopsis](server_module.md#id1)

- Create, update, start, stop and delete servers on the cloudscale.ch IaaS service.

Aliases: cloudscale_server

## [Parameters](server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **bulk_volume_size_gb**  integer | Size of the bulk storage volume in GB.  No bulk storage volume if not set. |
| **flavor**  string | Flavor of the server. |
| **force**  boolean | Allow to stop the running server for updating if necessary.  **Choices:**   - `false` ← (default) - `true` |
| **image**  string | Image used to create the server. |
| **interfaces**  list / elements=dictionary  *added in cloudscale_ch.cloud 1.4.0* | List of network interface objects specifying the interfaces to be attached to the server. See <https://www.cloudscale.ch/en/api/v1/#interfaces-attribute-specification> for more details. |
| **addresses**  list / elements=dictionary | Attach a private network interface and configure a subnet and/or an IP address. |
| **address**  string | The static IP address of the interface. Use ‘[]’ to avoid assigning an IP address via DHCP. |
| **subnet**  string | UUID of the subnet from which an address will be assigned. |
| **network**  string | Create a network interface on the network identified by UUID. Use ‘public’ instead of an UUID to attach a public network interface. Can be omitted if a subnet is provided under addresses. |
| **name**  string | Name of the Server.  Either *name* or *uuid* are required. |
| **password**  string | Password for the server. |
| **server_groups**  list / elements=string | List of UUID or names of server groups. |
| **ssh_keys**  list / elements=string | List of SSH public keys.  Use the full content of your .pub file here. |
| **state**  string | State of the server.  **Choices:**   - `"running"` ← (default) - `"stopped"` - `"absent"` |
| **tags**  dictionary | Tags assosiated with the servers. Set this to `{}` to clear any tags. |
| **use_ipv6**  boolean | Enable IPv6 on the public network interface.  **Choices:**   - `false` - `true` ← (default) |
| **use_private_network**  boolean | Attach a private network interface to the server.  **Choices:**   - `false` - `true` |
| **use_public_network**  boolean | Attach a public network interface to the server.  **Choices:**   - `false` - `true` |
| **user_data**  string | Cloud-init configuration (cloud-config) data to use for the server. |
| **uuid**  string | UUID of the server.  Either *name* or *uuid* are required. |
| **volume_size_gb**  integer | Size of the root volume in GB.  **Default:** `10` |
| **zone**  string | Zone in which the server resides (e.g. `lpg1` or `rma1`). |

## [Notes](server_module.md#id3)

> **Note:**
>
> - If *uuid* option is provided, it takes precedence over *name* for server selection. This allows to update the server’s name.
> - If no *uuid* option is provided, *name* is used for server selection. If more than one server with this name exists, execution is aborted.
> - Only the *name* and *flavor* are evaluated for the update.
> - The option *force=true* must be given to allow the reboot of existing running servers for applying the changes.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](server_module.md#id4)

```yaml+jinja
# Create and start a server with an existing server group (shiny-group)
- name: Start cloudscale.ch server
  cloudscale_ch.cloud.server:
    name: my-shiny-cloudscale-server
    image: debian-10
    flavor: flex-4-4
    ssh_keys:
      - ssh-rsa XXXXXXXXXX...XXXX ansible@cloudscale
    server_groups: shiny-group
    zone: lpg1
    use_private_network: true
    bulk_volume_size_gb: 100
    api_token: xxxxxx

# Start another server in anti-affinity (server group shiny-group)
- name: Start second cloudscale.ch server
  cloudscale_ch.cloud.server:
    name: my-other-shiny-server
    image: ubuntu-16.04
    flavor: flex-8-2
    ssh_keys:
      - ssh-rsa XXXXXXXXXX...XXXX ansible@cloudscale
    server_groups: shiny-group
    zone: lpg1
    api_token: xxxxxx

# Force to update the flavor of a running server
- name: Start cloudscale.ch server
  cloudscale_ch.cloud.server:
    name: my-shiny-cloudscale-server
    image: debian-10
    flavor: flex-8-2
    force: true
    ssh_keys:
      - ssh-rsa XXXXXXXXXX...XXXX ansible@cloudscale
    use_private_network: true
    bulk_volume_size_gb: 100
    api_token: xxxxxx
  register: server1

# Stop the first server
- name: Stop my first server
  cloudscale_ch.cloud.server:
    uuid: '{{ server1.uuid }}'
    state: stopped
    api_token: xxxxxx

# Delete my second server
- name: Delete my second server
  cloudscale_ch.cloud.server:
    name: my-other-shiny-server
    state: absent
    api_token: xxxxxx

# Start a server and wait for the SSH host keys to be generated
- name: Start server and wait for SSH host keys
  cloudscale_ch.cloud.server:
    name: my-cloudscale-server-with-ssh-key
    image: debian-10
    flavor: flex-4-2
    ssh_keys:
      - ssh-rsa XXXXXXXXXX...XXXX ansible@cloudscale
    api_token: xxxxxx
  register: server
  until: server is not failed
  retries: 5
  delay: 2

# Start a server with two network interfaces:
#
#    A public interface with IPv4/IPv6
#    A private interface on a specific private network with an IPv4 address

- name: Start a server with a public and private network interface
  cloudscale_ch.cloud.server:
    name: my-cloudscale-server-with-two-network-interfaces
    image: debian-10
    flavor: flex-4-2
    ssh_keys:
      - ssh-rsa XXXXXXXXXX...XXXX ansible@cloudscale
    api_token: xxxxxx
    interfaces:
      - network: 'public'
      - addresses:
        - subnet: UUID_of_private_subnet

# Start a server with a specific IPv4 address from subnet range
- name: Start a server with a specific IPv4 address from subnet range
  cloudscale_ch.cloud.server:
    name: my-cloudscale-server-with-specific-address
    image: debian-10
    flavor: flex-4-2
    ssh_keys:
      - ssh-rsa XXXXXXXXXX...XXXX ansible@cloudscale
    api_token: xxxxxx
    interfaces:
      - addresses:
        - subnet: UUID_of_private_subnet
          address: 'A.B.C.D'

# Start a server with two network interfaces:
#
#    A public interface with IPv4/IPv6
#    A private interface on a specific private network with no IPv4 address

- name: Start a server with a private network interface and no IP address
  cloudscale_ch.cloud.server:
    name: my-cloudscale-server-with-specific-address
    image: debian-10
    flavor: flex-4-2
    ssh_keys:
      - ssh-rsa XXXXXXXXXX...XXXX ansible@cloudscale
    api_token: xxxxxx
    interfaces:
      - network: 'public'
      - network: UUID_of_private_network
        addresses: []
```

## [Return Values](server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **flavor**  dictionary | The flavor that has been used for this server  **Returned:** success when not state == absent  **Sample:** `{"memory_gb": 4, "name": "Flex-4-2", "slug": "flex-4-2", "vcpu_count": 2}` |
| **href**  string | API URL to get details about this server  **Returned:** success when not state == absent  **Sample:** `"https://api.cloudscale.ch/v1/servers/cfde831a-4e87-4a75-960f-89b0148aa2cc"` |
| **image**  dictionary | The image used for booting this server  **Returned:** success when not state == absent  **Sample:** `{"default_username": "ubuntu", "name": "Ubuntu 18.04 LTS", "operating_system": "Ubuntu", "slug": "ubuntu-18.04"}` |
| **interfaces**  list / elements=string | List of network ports attached to the server  **Returned:** success when not state == absent  **Sample:** `[{"addresses": ["..."], "type": "public"}]` |
| **name**  string | The display name of the server  **Returned:** success  **Sample:** `"its-a-me-mario.cloudscale.ch"` |
| **server_groups**  list / elements=string | List of server groups  **Returned:** success when not state == absent  **Sample:** `[{"href": "https://api.cloudscale.ch/v1/server-groups/...", "name": "db-group", "uuid": "..."}]` |
| **ssh_fingerprints**  list / elements=string | A list of SSH host key fingerprints. Will be null until the host keys could be retrieved from the server.  **Returned:** success when not state == absent  **Sample:** `["ecdsa-sha2-nistp256 SHA256:XXXX", "..."]` |
| **ssh_host_keys**  list / elements=string | A list of SSH host keys. Will be null until the host keys could be retrieved from the server.  **Returned:** success when not state == absent  **Sample:** `["ecdsa-sha2-nistp256 XXXXX", "..."]` |
| **state**  string | The current status of the server  **Returned:** success  **Sample:** `"running"` |
| **tags**  dictionary | Tags assosiated with the server.  **Returned:** success  **Sample:** `{"project": "my project"}` |
| **uuid**  string | The unique identifier for this server  **Returned:** success  **Sample:** `"cfde831a-4e87-4a75-960f-89b0148aa2cc"` |
| **volumes**  list / elements=string | List of volumes attached to the server  **Returned:** success when not state == absent  **Sample:** `[{"device": "/dev/vda", "size_gb": "50", "type": "ssd"}]` |
| **zone**  dictionary | The zone used for booting this server  **Returned:** success when not state == absent  **Sample:** `{"slug": "lpg1"}` |

### Authors

- Gaudenz Steinlin (@gaudenz)
- René Moser (@resmo)
- Denis Krienbühl (@href)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
