---
collection: ansible
version: "8"
title: "openstack.cloud.lb_listener module – Manage load-balancer listener in a OpenStack cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/lb_listener_module.html
fetched_at: 2026-07-28T02:48:10+00:00
---
# openstack.cloud.lb_listener module – Manage load-balancer listener in a OpenStack cloud

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](lb_listener_module.md#ansible-collections-openstack-cloud-lb-listener-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.lb_listener`.

- [Synopsis](lb_listener_module.md#synopsis)
- [Requirements](lb_listener_module.md#requirements)
- [Parameters](lb_listener_module.md#parameters)
- [Notes](lb_listener_module.md#notes)
- [Examples](lb_listener_module.md#examples)
- [Return Values](lb_listener_module.md#return-values)

## [Synopsis](lb_listener_module.md#id1)

- Add, update or remove listener from OpenStack load-balancer.

## [Requirements](lb_listener_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](lb_listener_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **default_tls_container_ref**  string | A URI to a key manager service secrets container with TLS secrets. |
| **description**  string | A human-readable description for the load-balancer listener. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_admin_state_up**  boolean | The administrative state of the listener, which is up or down.  **Choices:**   - `false` - `true` |
| **load_balancer**  aliases: loadbalancer  string | The name or id of the load-balancer that this listener belongs to.  Required when *state* is `present`.  This attribute cannot be updated. |
| **name**  string / required | Name that has to be given to the listener.  This attribute cannot be updated. |
| **protocol**  string | The protocol for the listener.  For example, *protocol* could be `HTTP`, `HTTPS`, `TCP`, `TERMINATED_HTTPS`, `UDP`, `SCTP` or `PROMETHEUS`.  This attribute cannot be updated.  **Default:** `"HTTP"` |
| **protocol_port**  integer | The protocol port number for the listener.  This attribute cannot be updated. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **sni_container_refs**  list / elements=string | A list of URIs to the key manager service secrets containers with TLS secrets. |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **timeout_client_data**  integer | Client inactivity timeout in milliseconds. |
| **timeout_member_data**  integer | Member inactivity timeout in milliseconds. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](lb_listener_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](lb_listener_module.md#id5)

```yaml+jinja
- name: Create a listener, wait for the loadbalancer to be active
  openstack.cloud.lb_listener:
    cloud: mycloud
    load_balancer: test-loadbalancer
    name: test-listener
    protocol: HTTP
    protocol_port: 8080
    state: present

- name: Delete a listener
  openstack.cloud.lb_listener:
    cloud: mycloud
    load_balancer: test-loadbalancer
    name: test-listener
    state: absent

- name: Create a listener, increase timeouts for connection persistence
  openstack.cloud.lb_listener:
    cloud: mycloud
    load_balancer: test-loadbalancer
    name: test-listener
    protocol: TCP
    protocol_port: 22
    state: present
    timeout_client_data: 1800000
    timeout_member_data: 1800000
```

## [Return Values](lb_listener_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **listener**  dictionary | Dictionary describing the listener.  **Returned:** On success when *state* is `present`. |
| **allowed_cidrs**  list / elements=string | List of IPv4 or IPv6 CIDRs.  **Returned:** success |
| **alpn_protocols**  list / elements=string | List of ALPN protocols.  **Returned:** success |
| **connection_limit**  string | The maximum number of connections permitted for this load balancer.  **Returned:** success |
| **created_at**  string | Timestamp when the listener was created.  **Returned:** success |
| **default_pool**  string | Default pool to which the requests will be routed.  **Returned:** success |
| **default_pool_id**  string | ID of default pool. Must have compatible protocol with listener.  **Returned:** success |
| **default_tls_container_ref**  string | A reference to a container of TLS secrets.  **Returned:** success |
| **description**  string | The listener description.  **Returned:** success  **Sample:** `"description"` |
| **id**  string | Unique UUID.  **Returned:** success  **Sample:** `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |
| **insert_headers**  dictionary | Dictionary of additional headers insertion into HTTP header.  **Returned:** success |
| **is_admin_state_up**  boolean | The administrative state of the listener.  **Returned:** success  **Sample:** `true` |
| **l7_policies**  list / elements=string | A list of L7 policy objects.  **Returned:** success |
| **load_balancer_id**  string | The load balancer UUID this listener belongs to.  **Returned:** success  **Sample:** `"b32eef7e-d2a6-4ea4-a301-60a873f89b3b"` |
| **load_balancers**  list / elements=string | A list of load balancer IDs.  **Returned:** success  **Sample:** `[{"id": "b32eef7e-d2a6-4ea4-a301-60a873f89b3b"}]` |
| **name**  string | Name given to the listener.  **Returned:** success  **Sample:** `"test"` |
| **operating_status**  string | The operating status of the listener.  **Returned:** success  **Sample:** `"ONLINE"` |
| **project_id**  string | The ID of the project owning this resource.  **Returned:** success |
| **protocol**  string | The protocol for the listener.  **Returned:** success  **Sample:** `"HTTP"` |
| **protocol_port**  integer | The protocol port number for the listener.  **Returned:** success  **Sample:** `80` |
| **provisioning_status**  string | The provisioning status of the listener.  **Returned:** success  **Sample:** `"ACTIVE"` |
| **sni_container_refs**  list / elements=string | A list of references to TLS secrets.  **Returned:** success |
| **tags**  list / elements=string | A list of associated tags.  **Returned:** success |
| **timeout_client_data**  integer | Client inactivity timeout in milliseconds.  **Returned:** success  **Sample:** `50000` |
| **timeout_member_connect**  integer | Backend member connection timeout in milliseconds.  **Returned:** success |
| **timeout_member_data**  integer | Member inactivity timeout in milliseconds.  **Returned:** success  **Sample:** `50000` |
| **timeout_tcp_inspect**  integer | Time, in milliseconds, to wait for additional TCP packets for content inspection.  **Returned:** success |
| **tls_ciphers**  string | Stores a cipher string in OpenSSL format.  **Returned:** success |
| **tls_versions**  list / elements=string | A list of TLS protocols to be used by the listener.  **Returned:** success |
| **updated_at**  string | Timestamp when the listener was last updated.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
